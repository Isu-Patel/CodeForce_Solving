import sys

input = sys.stdin.readline

n = int(input())
q = [0] + list(map(int, input().split()))
m = int(input())
incoming = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    incoming[b].append((c, a))

roots = []
for i in range(1, n+1):
    if not incoming[i]:
        roots.append(i)

if len(roots) != 1:
    print(-1)
else:
    root = roots[0]
    total = 0
    possible = True
    for i in range(1, n+1):
        if i == root:
            continue
        if not incoming[i]:
            possible = False
            break
        total += min(c for c, a in incoming[i])
    if possible:
        print(total)
    else:
        print(-1)

