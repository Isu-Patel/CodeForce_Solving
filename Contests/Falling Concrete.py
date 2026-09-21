# Hi myslef Isu Patel.I solve and submit Codeforces comeptition ac solutions.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ballast = 0

    keys = set()

    for i in range(n):
        keys.add(a[i] - (i + 1))

    ans = 1

    for x in keys:
        if x + 1 not in keys:
            length = 1
            while x - length in keys:
                length += 1

            ans = max(ans, length)

    print(ans)