n, m, c = input().split()
n = int(n)
m = int(m)

grid = [input().strip() for _ in range(n)]

deputies = set()

# directions: up, down, left, right
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == c:
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                
                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] != '.' and grid[ni][nj] != c:
                        deputies.add(grid[ni][nj])

print(len(deputies))

