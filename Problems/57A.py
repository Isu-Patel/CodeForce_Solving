n, x1, y1, x2, y2 = map(int, input().split())


def position(x, y):
    if y == 0:
        return x

    if x == n:
        return n + y

    if y == n:
        return 3 * n - x

    return 4 * n - y


p1 = position(x1, y1)
p2 = position(x2, y2)

d = abs(p1 - p2)

print(min(d, 4 * n - d))