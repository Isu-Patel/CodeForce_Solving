import sys

input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
grid = []
index = 2
for i in range(n):
    row = data[index]
    grid.append(list(row))
    index += 1

# precompute prefix sum of 1s
prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + (1 if grid[i - 1][j - 1] == '1' else 0)

# find max perimeter
max_perim = 0
for i1 in range(n):
    for i2 in range(i1, n):
        for j1 in range(m):
            for j2 in range(j1, m):
                # sum of 1s in [i1..i2][j1..j2]
                ones = prefix[i2 + 1][j2 + 1] - prefix[i2 + 1][j1] - prefix[i1][j2 + 1] + prefix[i1][j1]
                if ones == 0:
                    h = i2 - i1 + 1
                    w = j2 - j1 + 1
                    perim = 2 * (h + w)
                    if perim > max_perim:
                        max_perim = perim

print(max_perim)