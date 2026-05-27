import math

n = int(input())

targets = []

for _ in range(n):
    x, y, t, p = input().split()

    x = int(x)
    y = int(y)
    t = int(t)
    p = float(p)

    targets.append((x, y, t, p))


targets.sort()

dp = [0.0] * n

ans = 0.0

for i in range(n):
    ti, xi, yi, pi = targets[i]

    # start directly from anywhere at time 0
    dp[i] = pi

    for j in range(i):
        tj, xj, yj, pj = targets[j]

        # Euclidean distance
        dist = math.hypot(xi - xj, yi - yj)

        # can move in time
        if dist <= ti - tj + 1e-9:
            dp[i] = max(dp[i], dp[j] + pi)

    ans = max(ans, dp[i])

print("{:.10f}".format(ans))