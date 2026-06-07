# Hello CodeForces. I solve CodeForce problems and submit on github for people for easy to check code.
# My Self Isu Patel. I am 15 yrs old who loves to do Coding and solving problems.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    z = input().strip()

    same1 = 0
    diff10 = 0
    diff01 = 0

    for a, b in zip(s, z):
        if a == '1' and b == '1':
            same1 += 1
        elif a == '1' and b == '0':
            diff10 += 1
        elif a == '0' and b == '1':
            diff01 += 1

    p0 = same1 + diff10
    p1 = same1 + diff01
    p2 = diff10 + diff01

    m = (1 << k) + 1

    cnt0 = (m + 2) // 3
    cnt1 = (m + 1) // 3
    cnt2 = m // 3

    ans = {
        cnt0 * p0 * (n - p0) +
        cnt1 * p1 * (n - p1) +
        cnt2 * p2 * (n - p2)
    }

    print(ans)
