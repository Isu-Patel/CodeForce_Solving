import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n = int(input())

g = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

leaf_order = list(map(int, input().split()))

# priority of leaves
pos = {}

for i, x in enumerate(leaf_order):
    pos[x] = i

INF = 10**9

# sort children according to leaf priority
def get_priority(x, p):
    # leaf
    if len(g[x]) == 1 and x != 1:
        return pos.get(x, INF)

    best = INF

    for nei in g[x]:
        if nei != p:
            best = min(best, get_priority(nei, x))

    return best

priority = [INF] * (n + 1)

def dfs_priority(u, p):
    if len(g[u]) == 1 and u != 1:
        priority[u] = pos[u]
        return priority[u]

    best = INF

    for v in g[u]:
        if v != p:
            best = min(best, dfs_priority(v, u))

    priority[u] = best
    return best

dfs_priority(1, 0)

for i in range(1, n + 1):
    g[i].sort(key=lambda x: priority[x])

route = []
seen_leaves = []

def dfs(u, p):
    route.append(u)

    is_leaf = (u != 1 and len(g[u]) == 1)

    if is_leaf:
        seen_leaves.append(u)

    for v in g[u]:
        if v != p:
            dfs(v, u)
            route.append(u)

dfs(1, 0)

if seen_leaves != leaf_order:
    print(-1)
else:
    print(*route)