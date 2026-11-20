import sys
import math
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

points = [
    tuple(map(float, input().split()))
    for _ in range(n + 1)
]

vp, vs = map(float, input().split())
P = tuple(map(float, input().split()))

cum =[0.0]

for i in range(n):
    a = points[i]
    b = points[i + 1]

    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dz = b[2] - a[2]

    length = math.sqrt(dx * dx + dy * dy + dz * dz)
    cum.append(cum[-1] + length)

total_time = cum[-1] / vs

def get_position(t):
    d = vs * t

    idx = bisect_left(cum, d)

    if idx == 0:
        return points[0]

    if idx >= n + 1:
        return points[n]

    i = idx - 1

    segment_length = cum[i + 1] - cum[i]
    ratio = (d - cum[i]) / segment_length

    a = points[i]
    b = points[i + 1]

    return (
        a[0] + (b[0] - a[0]) * ratio,
        a[1] + (b[1] - a[1]) * ratio,
        a[2] + (b[2] - a[2]) * ratio
    )

def can_catch(t):
    x, y, z = get_position(t)

    dx = x - P[0]
    dy = y - P[1]
    dz = z - P[2]

    distance_sq = dx * dx + dy * dy + dz * dz
    reachable_sq = (vp * t) ** 2

    return distance_sq <= reachable_sq

if not can_catch(total_time):
    print("NO")
    sys.exit()

low = 0.0
high = total_time

for _ in range(100):
    mid = (low + high) / 2

    if can_catch(mid):
        high = mid
    else:
        low = mid

t = high
x, y, z = get_position(t)

print("YES")
print(f"{t:.10f}")
print(f"{x:.10f} {y:.10f} {z:.10f}")