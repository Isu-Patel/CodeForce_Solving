from collections import defaultdict

n = int(input())

graph = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

# find endpoint (degree 1)
start = None

for node in graph:
    if len(graph[node]) == 1:
        start = node
        break

# reconstruct path
path = []
prev = -1
cur = start

while True:
    path.append(cur)
    
    nxt = None
    
    for nei in graph[cur]:
        if nei != prev:
            nxt = nei
            break
    
    if nxt is None:
        break
    
    prev, cur = cur, nxt

print(*path)