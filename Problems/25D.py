import sys

n = int(sys.stdin.readline().strip())
edges = []
adj = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    edges.append((u, v))
    adj[u].append((v, i))
    adj[v].append((u, i))

visited = [False] * n
comp_rep = []
tree_edge = [False] * (n - 1)

for i in range(n):
    if not visited[i]:
        comp_rep.append(i)
        stack = [i]
        visited[i] = True
        while stack:
            u = stack.pop()
            for v, ei in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    tree_edge[ei] = True
                    stack.append(v)

cand_edges = []
for i, (u, v) in enumerate(edges):
    if not tree_edge[i]:
        cand_edges.append((u, v))

t = len(comp_rep) - 1
print(t)
for idx in range(1, len(comp_rep)):
    u, v = cand_edges[idx - 1]
    print(u + 1, v + 1, comp_rep[0] + 1, comp_rep[idx] + 1)