n = int(input())

visited = set()
pos = 0

for k in range(1, 2 * n + 1):
    pos = (pos + k) % n
    visited.add(pos)

if len(visited) == n:
    print("YES")
else:
    print("NO")