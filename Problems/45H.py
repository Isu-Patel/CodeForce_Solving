import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    
    adj = [[] for _ in range(n+1)]
    edges = []
    for i in range(m):
        a = int(input_data[idx]); idx+=1
        b = int(input_data[idx]); idx+=1
        edges.append((a,b))
        adj[a].append((b,i))
        adj[b].append((a,i))
    
    disc = [0]*(n+1)
    low = [0]*(n+1)
    visited = [False]*(n+1)
    timer = [1]
    bridges = set()
    parent_edge = [-1]*(n+1)
    
    
    for start in range(1, n+1):
        if visited[start]:
            continue
        stack = [(start, -1, iter(adj[start]))]
        visited[start] = True
        disc[start] = low[start] = timer[0]
        timer[0]+=1
        while stack:
            node, pe, it = stack[-1]
            found_child = False
            for nxt, eid in it:
                if eid == pe:
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    disc[nxt] = low[nxt] = timer[0]
                    timer[0]+=1
                    stack.append((nxt, eid, iter(adj[nxt])))
                    found_child = True
                    break
                else:
                    if disc[nxt] < low[node]:
                        low[node] = disc[nxt]
            if found_child:
                continue
            stack.pop()
            if stack:
                pnode, ppe, pit = stack[-1]
                if low[node] < low[pnode]:
                    low[pnode] = low[node]
                if low[node] > disc[pnode]:
                    bridges.add(pe)
    
    parent = list(range(n+1))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(x,y):
        rx,ry = find(x), find(y)
        if rx!=ry:
            parent[rx]=ry
    
    for i,(a,b) in enumerate(edges):
        if i not in bridges:
            union(a,b)
    

    comp = {}
    def get_comp(x):
        r = find(x)
        if r not in comp:
            comp[r] = len(comp)
        return comp[r]
    
    tree_adj = {}
    for i in range(n+1):
        if i>=1:
            find(i)
    
    tree_edges = []
    for i,(a,b) in enumerate(edges):
        if i in bridges:
            ca, cb = get_comp(a), get_comp(b)
            tree_edges.append((ca,cb))
    
    num_comp = len(comp)
    
    if num_comp <= 1:
        print(0)
        return
    
    tadj = [[] for _ in range(num_comp)]
    for a,b in tree_edges:
        tadj[a].append(b)
        tadj[b].append(a)
    

    degree = [len(tadj[i]) for i in range(num_comp)]
    leaves = [i for i in range(num_comp) if degree[i]==1]
    
    
    rep = [-1]*num_comp
    for i in range(1, n+1):
        c = get_comp(i)
        if rep[c]==-1:
            rep[c]=i
    
    root = 0
    order = []
    visited2 = [False]*num_comp
    stack = [root]
    visited2[root]=True
    parent_arr = [-1]*num_comp
    dfs_order = []
    while stack:
        node = stack.pop()
        dfs_order.append(node)
        for nxt in tadj[node]:
            if not visited2[nxt]:
                visited2[nxt]=True
                parent_arr[nxt]=node
                stack.append(nxt)
    
    leaves_ordered = [i for i in dfs_order if degree[i]==1 and i!=root or (i==root and degree[i]==0)]
    
    if degree[root]==1:
        if root not in leaves_ordered:
            leaves_ordered.append(root)
    
    leaves_ordered = list(dict.fromkeys(leaves_ordered))
    
    L = len(leaves_ordered)
    added = []
    half = (L+1)//2
    for i in range(half):
        u = leaves_ordered[i]
        v = leaves_ordered[i+half] if i+half < L else leaves_ordered[0]
        if u==v:
            v = leaves_ordered[(i+half+1)%L] if L>1 else u
        added.append((rep[u], rep[v]))
    
    print(len(added))
    out = []
    for a,b in added:
        out.append(f"{a} {b}")
    print("\n".join(out))

main()