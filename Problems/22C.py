import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
v = int(data[2])

if m < 2 * n - 4:
    print(-1)
    sys.exit(0)

# Determine groupA and groupB
if v == 1:
    groupA = [2]
    groupB = list(range(3, n + 1))
elif v == n:
    groupA = list(range(1, n - 1))
    groupB = [n - 1]
else:
    groupA = list(range(1, v))
    groupB = list(range(v + 1, n + 1))

edges = []

# Connect v to all in groupA and groupB
for server in groupA + groupB:
    edges.append((v, server))

# Connect groupA in a path
for i in range(len(groupA) - 1):
    edges.append((groupA[i], groupA[i + 1]))

# Connect groupB in a path
for i in range(len(groupB) - 1):
    edges.append((groupB[i], groupB[i + 1]))

# Output the edges
for edge in edges:
    print(edge[0], edge[1])