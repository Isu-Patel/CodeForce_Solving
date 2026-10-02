from collections import deque

k, n, m = map(int, input().split())

grid = []
for _ in range(k):
    layer = []
    while len(layer) < n:
        line = input().strip()
        if line:
            layer.append(line)

    grid.append(layer)

x, y = map(int, input().split())
x -= 1
y -= 1

q = deque([(0, x, y)])
visited = [[[False] * m for _ in range(n)] for _ in range(k)]
visited[0][x][y] = True

answer = 0

directions = [
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1)
]

while q:
    z, r, c = q.popleft()
    answer += 1

    for dz, dr, dc in directions:
        nz = z + dz
        nr = r + dr
        nc = c + dc

        if not (0 <= nz < k and 0 <= nr < n and 0 <= nc < m):
            continue

        if visited[nz][nr][nc]:
            continue

        if grid[nz][nr][nc] == '#':
            continue

        visited[nz][nr][nc] = True
        q.append((nz, nr, nc))

print(answer)