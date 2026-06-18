from collections import deque

n, r1, r2 = map(int, input().split())

par = [0] * (n + 1)

vals = list(map(int, input().split()))
idx = 0

for i in range(1, n + 1):
    if i == r1:
        continue
    par[i] = vals[idx]
    idx += 1

g = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == r1:
        continue
    p = par[i]
    g[i].append(p)
    g[p].append(i)

new_par = [0] * (n + 1)

q = deque([r2])
visited = [False] * (n + 1)
visited[r2] = True

while q:
    u = q.popleft()

    for v in g[u]:
        if not visited[v]:
            visited[v] = True
            new_par[v] = u
            q.append(v)

ans = []

for i in range(1, n + 1):
    if i == r2:
        continue
    ans.append(str(new_par[i]))

print(" ".join(ans))
