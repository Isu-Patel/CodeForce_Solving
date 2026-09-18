import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

for _ in range(k):
    x, y = map(int, input().split())

    dist = min(x - 1, n - x, y - 1, m - y)

    if dist <= 4:
        print("YES")

        sys.exit()

print("NO")
