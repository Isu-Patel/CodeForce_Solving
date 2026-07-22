s = input().strip()
a = list(map(int, s))
n = len(a)

dp = [[0] * 10 for _ in range(n)]

# First digit can be anything
for d in range(10):
    dp[0][d] = 1

for i in range(1, n):
    for prev in range(10):
        if dp[i - 1][prev] == 0:
            continue
        sm = prev + a[i]
        if sm % 2 == 0:
            dp[i][sm // 2] += dp[i - 1][prev]
        else:
            dp[i][sm // 2] += dp[i - 1][prev]
            dp[i][sm // 2 + 1] += dp[i - 1][prev]

ans = sum(dp[n - 1])

# Check whether Masha's own number is among them
own = True
for i in range(1, n):
    if abs(a[i] - a[i - 1]) > 1:
        own = False
        break

if own:
    ans -= 1

print(ans)