n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

min_r, max_r = n, -1
min_c, max_c = m, -1

for i in range(n):
   for j in range(m):
      if grid[i][j] == '*':
         min_r = min(min_r, i)
         max_r = max(max_r, i)
         min_c = min(min_c, j)
         max_c = max(max_c, j)

for i in range(min_r, max_r + 1):
   print(grid[i][min_c:max_c + 1])
   