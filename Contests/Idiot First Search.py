import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input())

for _ in range(t):
    n = int(input())
    
    left = [0]*(n+1)
    right = [0]*(n+1)
    parent = [-1]*(n+1)
    
    for i in range(n):
        l, r = map(int, input().split())
        left[i] = l
        right[i] = r
        
        if l:
            parent[l] = i
        if r:
            parent[r] = i
    
    # build children list
    children = [[] for _ in range(n+1)]
    for i in range(n+1):
        if left[i]:
            children[i].append(left[i])
        if right[i]:
            children[i].append(right[i])
    
    # 1️⃣ compute subtree sizes
    sz = [0]*(n+1)
    
    def dfs1(v):
        sz[v] = 1
        for c in children[v]:
            dfs1(c)
            sz[v] += sz[c]
    
    dfs1(0)
    
    # 2️⃣ compute answers
    ans = [0]*(n+1)
    
    def dfs2(v):
        for c in children[v]:
            # move from v -> c
            ans[c] = (ans[v] + 1 + 2*(sz[v] - sz[c])) % MOD
            dfs2(c)
    
    dfs2(0)
    
    # output nodes 1..n
    print(*ans[1:])
