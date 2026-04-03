import sys
input = sys.stdin.readline

# Read input
xs, ys = map(int, input().split())
n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

# Distance squared
def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

# Precompute distances
d0 = [dist(xs, ys, x, y) for (x, y) in points]
d = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        d[i][j] = dist(points[i][0], points[i][1],
                       points[j][0], points[j][1])

# DP
N = 1 << n
INF = 10**18
dp = [INF] * N
parent = [(-1, -1)] * N

dp[0] = 0

for mask in range(N):
    if dp[mask] == INF:
        continue

    # find first unpicked object
    for i in range(n):
        if not (mask & (1 << i)):
            break
    else:
        continue

    # Take only i
    new_mask = mask | (1 << i)
    cost = dp[mask] + 2 * d0[i]
    if cost < dp[new_mask]:
        dp[new_mask] = cost
        parent[new_mask] = (i, -1)

    # Take i and j
    for j in range(i + 1, n):
        if not (mask & (1 << j)):
            new_mask2 = mask | (1 << i) | (1 << j)
            cost2 = dp[mask] + d0[i] + d[i][j] + d0[j]
            if cost2 < dp[new_mask2]:
                dp[new_mask2] = cost2
                parent[new_mask2] = (i, j)

# Output minimum cost
print(dp[N - 1])

# Reconstruct path
mask = N - 1
path = []

while mask:
    i, j = parent[mask]
    path.append(0)

    if j == -1:
        path.append(i + 1)
        mask ^= (1 << i)
    else:
        path.append(i + 1)
        path.append(j + 1)
        mask ^= (1 << i)
        mask ^= (1 << j)

path.append(0)
path.reverse()

print(*path)