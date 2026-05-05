import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
v = int(data[2])

min_m = 2 * n - 4
max_m = min_m + ((n - 3) * (n - 4) // 2)

if m < min_m or m > max_m:
    print(-1)
    sys.exit(0)

all_servers = [i for i in range(1, n + 1) if i != v]
groupA = [all_servers[0]]
groupB = all_servers[1:]

edges = []

# Connect v to all
for s in all_servers:
    edges.append((v, s))

# Path in groupB
for i in range(len(groupB) - 1):
    edges.append((groupB[i], groupB[i + 1]))

# Add extra edges in groupB
extra = m - len(edges)
idx = 0
for i in range(1, len(groupB)):
    if extra == 0:
        break
    edges.append((groupB[0], groupB[i]))
    extra -= 1

# Output the edges
for edge in edges:
    print(edge[0], edge[1])