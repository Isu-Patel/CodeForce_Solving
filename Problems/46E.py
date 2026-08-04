import sys

input = sys.stdin.readline

n, m = map(int, input().split())

NEG = -10**30

# First row
row = list(map(int, input().split()))
pref = [0] * (m + 1)
for i in range(1, m + 1):
    pref[i] = pref[i - 1] + row[i - 1]

dp = [NEG] * (m + 1)
for j in range(1, m + 1):
    dp[j] = pref[j]

for r in range(2, n + 1):
    row = list(map(int, input().split()))
    pref = [0] * (m + 1)
    for i in range(1, m + 1):
        pref[i] = pref[i - 1] + row[i - 1]

    ndp = [NEG] * (m + 1)

    if r % 2 == 0:
        # previous > current
        suf = [NEG] * (m + 2)
        for j in range(m, 0, -1):
            suf[j] = max(suf[j + 1], dp[j])
        for j in range(1, m + 1):
            if suf[j + 1] != NEG:
                ndp[j] = pref[j] + suf[j + 1]
    else:
        # previous < current
        pre = [NEG] * (m + 1)
        for j in range(1, m + 1):
            pre[j] = max(pre[j - 1], dp[j])
        for j in range(1, m + 1):
            if pre[j - 1] != NEG:
                ndp[j] = pref[j] + pre[j - 1]

    dp = ndp

print(max(dp[1:]))
