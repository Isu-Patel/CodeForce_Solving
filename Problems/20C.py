import heapq
import sys

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a = int(data[index])
    index += 1
    b = int(data[index])
    index += 1
    w = int(data[index])
    index += 1
    graph[a].append((b, w))
    graph[b].append((a, w))

dist = [float('inf')] * (n + 1)
dist[1] = 0
parent = [-1] * (n + 1)
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u
            heapq.heappush(pq, (dist[v], v))

if dist[n] == float("inf"):
    print(-1)

else:
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    print(' '.join(map(str, path)))
    
