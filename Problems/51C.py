import sys

input = sys.stdin.readline

n = int(input())
x = sorted(map(int, input().split()))


def can(d2):

    stations = 0
    i = 0

    while i < n:
        stations += 1

        if stations > 3:
            return False

        left = x[i]

        limit = 2 * left + d2

        i += 1

        while i < n and 2 * x[i] <= limit:
            i += 1

    return True


lo = 0
hi = 2 * (x[-1] - x[0])

while lo < hi:
    mid = (lo + hi) // 2

    if can(mid):
        hi = mid
    else:
        lo = mid + 1

d2 = lo


stations = []
i = 0

while i < n and len(stations) < 3:
    left = x[i]

    station2 = 2 * left + d2
    stations.append(station2)

    limit = 2 * left + d2

    i += 1

    while i < n and 2 * x[i] <= limit:
        i += 1

while len(stations) < 3:
    stations.append(stations[-1])


print(f"{d2 / 2:.6f}")

print(
    f"{stations[0] / 2:.6f} "
    f"{stations[1] / 2:.6f} "
    f"{stations[2] / 2:.6f}"
)