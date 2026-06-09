# Hi Everyone myself Isu Pate.
# I will solve every question of contest and post on github.
# My github ID is Isu-Patel.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    inc = list(range(1, n + 1))

    if n % 2 == 0:
        third = list(range(n, 0, -1))
    else:
        third = list(range(2, n + 1)) + [1]

    ans = inc + inc + third + inc

    print(*ans)