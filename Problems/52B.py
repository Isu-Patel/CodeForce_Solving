import sys

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

row_left = [[0] * m for _ in range(n)]
row_right = [[0] * m for _ in range(n)]
col_up = [[0] * m for _ in range(n)]
col_down = [[0] * m for _ in range(n)]

for i in range(n):
    cnt = 0

    for j in range(m):
        row_left[i][j] = cnt
        if grid[i][j] == "*":
            cnt += 1

    cnt = 0

    for j in range(m - 1, -1, -1):
        row_right[i][j] = cnt
        if grid[i][j] == "*":
            cnt += 1

for j in range(m):
    cnt = 0
    for i in range(n):
        col_up[i][j] = cnt
        if grid[i][j] == "*":
            cnt += 1

    cnt = 0
    for i in range(n - 1, -1, -1):
        col_down[i][j] = cnt
        if grid[i][j] == "*":
            cnt += 1

answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '*':
            horizontal = row_left[i][j] + row_right[i][j]
            vertical = col_up[i][j] + col_down[i][j]

            answer += horizontal * vertical

print(answer)