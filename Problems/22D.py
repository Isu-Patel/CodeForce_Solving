import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))
segments = []
for _ in range(n):
    a = int(next(it)); b = int(next(it))
    if a <= b:
        segments.append((a, b))
    else:
        segments.append((b, a))

segments.sort(key=lambda x: x[1])

points = []
i = 0

while i < n:
    _, r = segments[i]
    points.append(r)
    j = i + 1
    while j < n and segments[j][0] <= r:
        j += 1
    i = j

out = []
out.append(str(len(points)))
out.append(' '.join(map(str(x) for x in points)))
sys.stdout.write('\n'.join(out))