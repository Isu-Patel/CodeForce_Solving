# Hello Myself Isu Patel. I solve CodeForce problems and submit on github for people for easy to check code.
# This is Code is written by me only.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    ans = []

    for empty in range(n):
        m = n - 1

        # edges of the broken line
        e = [h[empty]]
        for j in range(1, m):
            e.append(h[(empty + j) % n])
        e.append(h[(empty - 1) % n])

        pref = [0] * (m + 1)
        pref[0] = e[0]
        for i in range(1, m + 1):
            pref[i] = max(pref[i - 1], e[i])

        suff = [0] * (m + 1)
        suff[m] = e[m]
        for i in range(m - 1, -1, -1):
            suff[i] = max(suff[i + 1], e[i])

        total = 0
        for p in range(m):
            total += min(pref[p], suff[p + 1])

        ans.append(total)

    print(*ans)