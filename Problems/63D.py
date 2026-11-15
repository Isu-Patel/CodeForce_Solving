import sys

input = sys.stdin.readline

a, b, c, d, n = map(int, input().split())
x = list(map(int, input().split()))

H = max(b, d)
W = a + c

if sum(x) != a * b + c * d:
    print("NO")
    sys.exit()

path = []
common = min(b, d)

if b > d:
    side = "left"
elif d > b:
    side = "right"
else:
    side = "none"

if side == "left":
    start_right = (common % 2 == 0)
elif side == "right":
    start_right = (common % 2 == 1)
else:
    start_right = True

for r in range(common):
    if start_right:
        cols = range(W)
    else:
        cols = range(W - 1, -1, -1)

    for col in cols:
        path.append((r, col))

    start_right = not start_right

if side == "left":
    left, right = 0, a - 1
elif side == "right":
    left, right = a, W - 1
else:
    left, right = 0, -1

for r in range(common, H):
    if left <= right:
        if start_right:
            cols = range(left, right + 1)
        else:
            cols = range(right, left - 1, -1)

        for col in cols:
            path.append((r, col))

        start_right = not start_right

grid = [['.'] * W for _ in range(H)]

pos = 0

for i in range(n):
    for _ in range(x[i]):
        r, col = path[pos]
        grid[r][col] = chr(ord('a') + i)
        pos += 1

print("YES")
for row in grid:
    print(''.join(row))