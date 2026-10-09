import sys
import math

input = sys.stdin.readline
EPS = 1e-9

n = int(input())
triangles = []
edges = []

for idx in range(n):
    v = list(map(int, input().split()))
    tri = [(v[i], v[i + 1]) for i in range(0, 6, 2)]

    xs = [p[0] for p in tri]
    ys = [p[1] for p in tri]
    box = (min(xs), max(xs), min(ys), max(ys))

    triangles.append((tri, box))

    for j in range(3):
        a = tri[j]
        b = tri[(j + 1) % 3]
        edges.append((idx, a, b))

def cross(ax, ay, bx, by):
    return ax * by - ay * bx

def inside(x, y, tri):
    p, q, r = tri

    c1 = cross(q[0] - p[0], q[1] - p[1],
               x - p[0], y - p[1])
    c2 = cross(r[0] - q[0], r[1] - q[1],
               x - q[0], y - q[1])
    c3 = cross(p[0] - r[0], p[1] - r[1],
               x - r[0], y - r[1])

    return ((c1 > EPS and c2 > EPS and c3 > EPS) or
            (c1 < -EPS and c2 < -EPS and c3 < -EPS))

def covered(x, y, owner):
    for idx, (tri, box) in enumerate(triangles):
        if idx == owner:
            continue

        xmin, xmax, ymin, ymax = box
        if (xmin + EPS < x < xmax - EPS or
            xmin - EPS <= x <= xmax + EPS) and \
           ymin - EPS <= y <= ymax + EPS:
            if inside(x, y, tri):
                return True

    return False

answer = 0.0

for owner, a, b in edges:
    ax, ay = a
    bx, by = b

    dx = bx - ax
    dy = by - ay
    length = math.hypot(dx, dy)

    ts = [0.0, 1.0]
    rr = dx * dx + dy * dy

    for other, c, d in edges:
        if other == owner:
            continue

        cx, cy = c
        ex, ey = d

        sx = ex - cx
        sy = ey - cy

        denom = cross(dx, dy, sx, sy)
        qx = cx - ax
        qy = cy - ay

        if denom != 0:
            t = cross(qx, qy, sx, sy) / denom
            u = cross(qx, qy, dx, dy) / denom

            if -EPS <= t <= 1 + EPS and -EPS <= u <= 1 + EPS:
                ts.append(max(0.0, min(1.0, t)))

        elif cross(qx, qy, dx, dy) == 0:
            for px, py in (c, d):
                t = ((px - ax) * dx + (py - ay) * dy) / rr
                if -EPS <= t <= 1 + EPS:
                    ts.append(max(0.0, min(1.0, t)))

    ts.sort()
    unique = []

    for t in ts:
        if not unique or t - unique[-1] > EPS:
            unique.append(t)

    for i in range(len(unique) - 1):
        t1 = unique[i]
        t2 = unique[i + 1]

        if t2 - t1 <= EPS:
            continue

        mid = (t1 + t2) / 2
        mx = ax + mid * dx
        my = ay + mid * dy

        if not covered(mx, my, owner):
            answer += length * (t2 - t1)

print(f"{answer:.10f}")