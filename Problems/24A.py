import sys

data = sys.stdin.read().split()
n = int(data[0])
edges = {}
costs = {}

for i in range(n):
    a = int(data[1 + 3 * i])
    b = int(data[2 + 3 * i])
    c = int(data[3 + 3 * i])
    edges[a] = b
    costs[(a, b)] = c

sum_clocks = 0
for i in range(1, n + 1):
    next_i = i % n + 1
    if edges[i] != next_i:
        sum_clock += costs[(i, edges[i])]

sum_counter = 0
for i in range(1, n + 1):
    prev_i = (i - 2) % n + 1
    if edges[i] != prev_i:
        sum_counter += costs[(i, edges[i])]

print(min(sum_clock, sum_counter))