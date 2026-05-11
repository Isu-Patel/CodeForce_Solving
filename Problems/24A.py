import sys
input = sys.stdin.readline

n = int(input())

# graph[u] = [(v, cost_if_reverse)]
graph = [[] for _ in range(n + 1)]

# store reverse costs
cost = {}

for _ in range(n):
    a, b, c = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

    # original direction a -> b
    # reversing it costs c
    cost[(a, b)] = 0
    cost[(b, a)] = c

# reconstruct the cycle order
cycle = [1]
prev = -1
cur = 1

while True:
    nxts = graph[cur]

    nxt = nxts[0] if nxts[0] != prev else nxts[1]

    if nxt == 1:
        break

    cycle.append(nxt)
    prev, cur = cur, nxt

# add start again for easy traversal
cycle.append(1)

# cost in this direction
cost1 = 0

for i in range(len(cycle) - 1):
    u = cycle[i]
    v = cycle[i + 1]

    cost1 += cost[(u, v)]

# opposite direction
total_reverse = 0

for (u, v), c in cost.items():
    if c > 0:
        total_reverse += c

cost2 = total_reverse - cost1

print(min(cost1, cost2))