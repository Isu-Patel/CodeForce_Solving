import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a] |= (1 << b)
    adj[b] |= (1 << a)

ans = 0

for start in range(n):
    dp = [{} for _ in range(1 << n)]
    dp[1 << start][start] = 1

    for mask in range(1 << n):
        if not (mask & (1 << start)):
            continue

        size = mask.bit_count()

        for u in list(dp[mask].keys()):
            ways = dp[mask][u]

            # neighbors of u
            for v in range(start, n):
                if not (adj[u] & (1 << v)):
                    continue

                if not (mask & (1 << v)):
                    dp[mask | (1 << v)][v] = dp[mask | (1 << v)].get(v, 0) + ways
                elif v == start and size >= 3:
                    ans += ways

print(ans // 2)