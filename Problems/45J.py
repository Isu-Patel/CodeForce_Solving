n, m = map(int, input().split())
if n == 1 and m == 1:
    print(1)
elif n == 1 or m == 1:
    print(-1)
else:
    grid = [[0]*m for _ in range(n)]
    order = []
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                order.append((i,j))
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 1:
                order.append((i,j))
    for idx, (i,j) in enumerate(order):
        grid[i][j] = idx+1
    print('\n'.join(' '.join(map(str,row)) for row in grid))