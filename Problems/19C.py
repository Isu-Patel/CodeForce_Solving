import sys

data = sys.stdin.read().split()
if not data:
    sys.exit(0)

n = int(data[0])
arr = list(map(int, data[1:]))

pos = {}
for i, v in enumerate(arr):
    pos.setdefault(v, []).append(i)

mask = (1 << 64) - 1
B1 = 1000003
B2 = 1000033

h1 = [0] * (n + 1)
p1 = [1] * (n + 1)
h2 = [0] * (n + 1)
p2 = [1] * (n + 1)

for i, x in enumerate(arr):
    v = x + 1
    h1[i + 1] = ((h1[i] * B1) + v) & mask
    h2[i + 1] = ((h2[i] * B2) + v) & mask
    p1[i + 1] = (p1[i] * B1) & mask
    p2[i + 1] = (p2[i] * B2) & mask

def hash_range(l, r):
    return (
        (h1[r] - h1[l] * p1[r - l]) & mask,
        (h2[r] - h2[l] * p2[r - l]) & mask,
    )

cands = []
for v, plist in pos.items():
    m = len(plist)
    for i in range(m):
        l = plist[i]
        for j in range(i + 1, m):
            x = plist[j] - l
            if l + 2 * x > n:
                break
            if hash_range(l, l + x) == hash_range(l + x, l + 2 * x):
                cands.append((x, l))

cands.sort()
start = 0
idx = 0
while True:
    while idx < len(cands) and cands[idx][1] < start:
        idx += 1
    if idx >= len(cands):
        break
    x, l = cands[idx]
    if l + 2 * x > n:
        idx += 1
        continue
    start = l + x
    idx += 1

remaining = arr[start:]
print(len(remaining))
if remaining:
    print(" ".join(str(x) for x in remaining))
