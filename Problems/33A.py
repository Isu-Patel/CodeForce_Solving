n, m, k = map(int, input().split())

INF = 10**18
row_min = [INF] * m

for _ in range(n):
    r, c = map(int, input().split())
    row_min[r - 1] = min(row_min[r - 1], c)

total = sum(row_min)

print(min(total, k))