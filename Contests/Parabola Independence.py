import sys
input = sys.stdin.readline

def independent(a1,b1,c1,a2,b2,c2):
    A = a1 - a2
    B = b1 - b2
    C = c1 - c2
    
    if A == 0:
        if B == 0:
            return C != 0  # constant nonzero
        return False       # linear → has root
    
    return B*B - 4*A*C < 0

t = int(input())

for _ in range(t):
    n = int(input())
    
    a = []
    b = []
    c = []
    
    for _ in range(n):
        ai,bi,ci = map(int,input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    
    # build DAG
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    indeg = [0]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if independent(a[i],b[i],c[i], a[j],b[j],c[j]):
                # decide order by value at x=0
                if c[i] > c[j]:
                    adj[i].append(j)
                    radj[j].append(i)
                    indeg[j] += 1
                else:
                    adj[j].append(i)
                    radj[i].append(j)
                    indeg[i] += 1
    
    # topological sort
    from collections import deque
    q = deque()
    
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    topo = []
    while q:
        v = q.popleft()
        topo.append(v)
        for u in adj[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    
    # longest path ending at i
    dp_in = [1]*n
    for v in topo:
        for u in adj[v]:
            dp_in[u] = max(dp_in[u], dp_in[v] + 1)
    
    # longest path starting at i
    dp_out = [1]*n
    for v in reversed(topo):
        for u in adj[v]:
            dp_out[v] = max(dp_out[v], dp_out[u] + 1)
    
    # answers
    ans = [dp_in[i] + dp_out[i] - 1 for i in range(n)]
    
    print(*ans)
