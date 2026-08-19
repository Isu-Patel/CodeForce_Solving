import sys

input = sys.stdin.readline


def cross(o, a, b):
    return (
        (a[0] - o[0]) * (b[1] - o[1])
        - (a[1] - o[1]) * (b[0] - o[0])
    )


def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    # Lower hull
    lower = []

    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()

        lower.append(p)

    # Upper hull
    upper = []

    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()

        upper.append(p)

    return lower[:-1] + upper[:-1]


n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())

    points.append((x + 1, y))
    points.append((x - 1, y))
    points.append((x, y + 1))
    points.append((x, y - 1))


hull = convex_hull(points)

answer = 0
k = len(hull)

for i in range(k):
    x1, y1 = hull[i]
    x2, y2 = hull[(i + 1) % k]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    answer += max(dx, dy)

print(answer)