import sys
from collections import deque

input = sys.stdin.readline

n, MAXH, reg = map(int, input().split())

scrolls = []
for i in range(n):
    p, d = map(int, input().split())
    scrolls.append((p, d, i + 1))

INF = 10**18

dp = [INF] * (MAXH + 1)
par = [None] * (MAXH + 1)

dp[MAXH] = 0

for h in range(MAXH, -1, -1):
    if dp[h] == INF:
        continue

    total_dmg = 0
    used = set()

    cur_time = dp[h]

    for p, d, idx in scrolls:
        if h * 100 <= p * MAXH:
            total_dmg += d

    if total_dmg <= reg:
        continue

    nh = h

    while nh > 0:
        nh -= (total_dmg - reg)
        if nh < 0:
            nh = 0

        if dp[nh] > cur_time + 1:
            dp[nh] = cur_time + 1
            par[nh] = h

    for p, d, idx in scrolls:
        if h * 100 <= p * MAXH:
            nh = h
            if dp[nh] > cur_time:
                dp[nh] = cur_time
                par[nh] = h

if dp[0] == INF:
    print("NO")
else:
    print("YES")
    print(dp[0], 0)