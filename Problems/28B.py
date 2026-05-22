n = int(input())
perm = list(map(int, input().split()))
d = list(map(int, input().split()))

adj = [set() for _ in range(n)]
for i in range(n):
    j1 = i + d[i]
    j2 = i - d[i]
    if 0 <= j1 < n:
        adj[i].add(j1)
        adj[j1].add(i)
    if 0 <= j2 < n:
        adj[i].add(j2)
        adj[j2].add(i)

visited = [False] * n
components = []

def dfs(node, component):
    visited[node] = True
    component.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, component)

for i in range(n):
    if not visited[i]:
        component = []
        dfs(i, component)
        components.append(component)

valid = True
for component in components:
    original_values = sorted([i + 1 for i in component])
    current_values = sorted([perm[i] for i in component])

    if original_values != current_values:
        valid = False
        break

if valid:
    print("YES")
else:
    print("NO")

