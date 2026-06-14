import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
circles = [tuple(map(int, input().split())) for _ in range(m)]

masks = [0] * n

for cid, (r, cx, cy) in enumerate(circles):
    rr = r * r
    bit = 1 << cid

    for i, (x, y) in enumerate(points):
        dx = x - cx
        dy = y - cy

        if dx * dx + dy * dy < rr:
            masks[i] |= bit

for _ in range(k):
    a, b = map(int, input().split())

    x = masks[a - 1] ^ masks[b - 1]

    print(x.bit_count())