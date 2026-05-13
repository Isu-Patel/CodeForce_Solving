import sys
input = sys.stdin.readline

n, j = map(int, input().split())

mx, my = map(int, input().split())

A = [tuple(map(int, input().split())) for _ in range(n)]

# period = 2n
j %= (2 * n)

x, y = mx, my

for i in range(j):
    ax, ay = A[i % n]

    # symmetry formula
    x = 2 * ax - x
    y = 2 * ay - y

print(x, y)