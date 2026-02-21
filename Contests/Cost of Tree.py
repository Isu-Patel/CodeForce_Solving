import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    parent = [0]*(n+1)
    depth = [0]*(n+1)
    sub = [0]*(n+1)
    
    # DFS build tree rooted at 1
    def dfs(u, p):
        parent[u] = p
        sub[u] = a[u]
        for v in adj[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            dfs(v, u)
            sub[u] += sub[v]
    
    dfs(1, 0)
    
    total = sub[1]
    
    # base cost for root 1
    cost = [0]*(n+1)
    cost[1] = sum(a[i]*depth[i] for i in range(1, n+1))
    
    # reroot dp
    def dfs2(u, p):
        for v in adj[u]:
            if v == p:
                continue
            cost[v] = cost[u] - sub[v] + (total - sub[v])
            dfs2(v, u)
    
    dfs2(1, 0)
    
    # compute best gain
    best = [0]*(n+1)
    
    def dfs3(u, p):
        best[u] = 0
        for v in adj[u]:
            if v == p:
                continue
            dfs3(v, u)
            best[u] = max(best[u], best[v])
            # gain pushing v deeper
            best[u] = max(best[u], sub[v])
    
    dfs3(1, 0)
    
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = cost[i] + best[i]
    
    print(*ans[1:])