import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    a = [0] + list(map(int, input().split()))
    b = set(map(int, input().split()))
    
    subxor = [0]*(n+1)
    
    def dfs(u, parent):
        subxor[u] = a[u]
        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)
            subxor[u] ^= subxor[v]
    
    dfs(1, 0)
    
    total_xor = subxor[1]
    
    good_vals = []
    for v in range(2, n+1):
        if subxor[v] in b:
            good_vals.append(subxor[v])
    
    if total_xor in b:
        # all subsets valid
        print(pow(2, len(good_vals), MOD))
        continue
    
    targets = set()
    for bi in b:
        targets.add(total_xor ^ bi)
    
    dp = {0: 1}
    
    for val in good_vals:
        new_dp = dp.copy()
        for x in dp:
            nx = x ^ val
            new_dp[nx] = (new_dp.get(nx, 0) + dp[x]) % MOD
        dp = new_dp
    
    ans = 0
    for target in targets:
        ans = (ans + dp.get(target, 0)) % MOD
    
    print(ans)
