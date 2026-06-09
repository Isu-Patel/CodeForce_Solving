# Hi Everyone myself Isu Pate. Im here today to solve this contest and ave a good and higher rating.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, y, z = map(int, input().split())

    no_ai = (n + (x + y) - 1) // (x + y)

    if x * z >= n:
        ai = (n + x - 1) // x
    else:
        rem = n - x * z
        ai = z + (rem + (x + 10 * y) - 1) // (x + 10 * y)

    print(min(no_ai, ai))