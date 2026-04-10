import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, x1, y1, x2, y2 = map(int, input().split())

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    reachable = (n - dx) * (m - dy)
    total = n * m

    print(total - reachable)