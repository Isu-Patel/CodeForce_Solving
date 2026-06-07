#Hi Myself Isu Patel and i am only 15 yrs old wo loves to do Coding and much more.
# I solve CodeForce problems and submit on github for people for easy to check code.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    ans = [0] * n

    for empty in range(n):
        m = n - 1

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

        cur = 0
        for i in range(m):
            cur += min(pref[i], suff[i + 1])

        ans[empty] = cur

    print(*ans)