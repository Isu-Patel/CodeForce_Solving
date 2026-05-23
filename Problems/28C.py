import sys
from math import comb

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

total_prob = m ** n

dp = {(0, 0): 1.0}

for idx in range(m):
    ndp = {}

    basins = a[idx]

    for (used, curmax), ways in dp.items():

        rem = n - used

        for x in range(rem + 1):
            # choose x students for this room
            ways_choose = comb(rem, x)

            # queue size in this room
            q = (x + basins - 1) // basins

            newmax = max(curmax, q)

            key = (used + x, newmax)

            ndp[key] = ndp.get(key, 0.0) + ways * ways_choose

    dp = ndp


ans = 0.0

fact = [1]
for i in range(1, n + 1):
    fact.append(fact[-1] * i)


for (used, mx), ways in dp.items():
    if used == n:
        ans += mx * ways / total_prob

print("{:.15f}".format(ans))    