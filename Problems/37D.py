MOD = 1000000007

m = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

n = sum(X)

fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact = [1] * (n + 1)
invfact[n] = pow(fact[n], MOD - 2, MOD)
for i in range(n, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

def C(a, b):
    if b < 0 or b > a:
        return 0
    return fact[a] * invfact[b] % MOD * invfact[a - b] % MOD

dp = [0] * (n + 1)
dp[0] = 1

for i in range(m):
    ndp = [0] * (n + 1)

    for used in range(n + 1):
        if dp[used] == 0:
            continue

        for take in range(X[i], Y[i] + 1):
            if used + take > n:
                break

            ndp[used + take] = (
                ndp[used + take]
                + dp[used] * C(n - used, take)
            ) % MOD

    dp = ndp

print(dp[n] % MOD)