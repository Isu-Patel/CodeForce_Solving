n = int(input())

a = n // 2
b = n - a

edges = []
for i in range(1, a + 1):
    for j in range(a + 1, n + 1):
        edges.append((i, j))

print(len(edges))
for u, v in edges:
    print(u, v)
    