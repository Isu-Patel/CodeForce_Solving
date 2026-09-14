import sys

input = sys.stdin.readline


def count_ones(x):
    if x <= 0:
        return 0

    ans = 0
    p = 1

    while p <= x:
        ans += max(0, min(x, 2 * p - 1) - p + 1)
        p *= 10

    return ans


n = int(input())

probs = []

for _ in range(n):
    L, R = map(int, input().split())

    total = R - L + 1
    ones = count_ones(R) - count_ones(L - 1)

    probs.append(ones / total)

K = int(input())

need = (n * K + 99) // 100

if need == 0:
    print("1.000000000000000")
    sys.exit()

if need > n:
    print("0.000000000000000")
    sys.exit()

dp = [0.0] * (need + 1)
dp[0] = 1.0

for p in probs:
    upper = min(need, n)

    for j in range(upper, 0, -1):
        dp[j] = dp[j] * (1.0 - p) + dp[j - 1] * p

    dp[0] *= (1.0 - p)

less = sum(dp[:need])

answer = 1.0 - less

print("{:.15f}".format(answer))