# IM doing this on my own and then posting it on gituhub

import sys
 
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref = 0
    cur = 10 ** 18

    ans = []

    for i in range(n):
        pref += a[i]
        cur = min(cur, pref // (i + 1))
        ans.append(cur)

    print(*ans)
