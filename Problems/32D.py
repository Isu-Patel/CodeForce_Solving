n, m, k = map(int, input().split())
g = [input().strip() for _ in range(n)]

# Maximum possible radius
R = min(n, m) // 2

# up[i][j], down[i][j], left[i][j], right[i][j]
up = [[0] * m for _ in range(n)]
down = [[0] * m for _ in range(n)]
left = [[0] * m for _ in range(n)]
right = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if g[i][j] == '*':
            up[i][j] = 1 + (up[i - 1][j] if i > 0 else 0)
            left[i][j] = 1 + (left[i][j - 1] if j > 0 else 0)

for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if g[i][j] == '*':
            down[i][j] = 1 + (down[i + 1][j] if i + 1 < n else 0)
            right[i][j] = 1 + (right[i][j + 1] if j + 1 < m else 0)

cnt = 0

for r in range(1, max(n, m) + 1):
    found = False

    for i in range(n):
        for j in range(m):
            if g[i][j] != '*':
                continue

            if (up[i][j] > r and down[i][j] > r and
                left[i][j] > r and right[i][j] > r):

                cnt += 1

                if cnt == k:
                    print(i + 1, j + 1)         # center
                    print(i + 1 - r, j + 1)     # up
                    print(i + 1 + r, j + 1)     # down
                    print(i + 1, j + 1 - r)     # left
                    print(i + 1, j + 1 + r)     # right
                    raise SystemExit

                found = True

    if not found:
        break

print(-1)