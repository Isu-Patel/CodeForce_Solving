# Hi Im doing on my own and posting on github to elp everyone practise

import sys

input = sys.stdin.readline

MAXN = 200000

spf = list(range(MAXN + 1))
for i in range(2, int(MAXN ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAXN + 1, i):
            if spf[j] == j:
                spf[j] = i


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [0] * (n + 1)

    for x in range(k + 1, n + 1):
        y = x
        best = 10**18

        while y > 1:
            p = spf[y]

            best = min(best, 1 + p * dp[x // p])

            while y % p == 0:
                y //= p

        dp[x] = best

    ans = sum(dp[x] for x in a)

    print(ans)