import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[False]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a][b] = adj[b][a] = True

ans = 0

for start in range(n):
    dp = [ [0]*n for _ in range(1 << n) ]
    dp[1 << start][start] = 1

    for mask in range(1 << n):
        if not (mask & (1 << start)):
            continue

        for u in range(n):
            if not (mask & (1 << u)):
                continue
            if dp[mask][u] == 0:
                continue

            for v in range(start, n):
                if not adj[u][v]:
                    continue

                if not (mask & (1 << v)):
                    dp[mask | (1 << v)][v] += dp[mask][u]
                elif v == start and bin(mask).count('1') >= 3:
                    ans += dp[mask][u]

print(ans // 2)