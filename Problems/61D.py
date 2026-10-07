import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
total = 0

for _ in range(n - 1):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
    graph[y].append((x, w))
    total += w

stack = [(1, 0, 0)]
max_dist = 0

while stack:
    u, parent, dist = stack.pop()
    max_dist = max(max_dist, dist)

    for v, w in graph[u]:
        if v != parent:
            stack.append((v, u, dist + w))

print(2 * total - max_dist)