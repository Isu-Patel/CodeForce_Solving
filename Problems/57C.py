import sys

MOD = 1000000007

n = int(sys.stdin.readline())

fact = [1] * (2 * n + 1)

for i in range(1, 2 * n + 1):
    fact[i] = fact[i - 1] * i % MOD

comb = (
    fact[2 * n - 1]
    * pow(fact[n], MOD - 2, MOD)
    % MOD
    * pow(fact[n - 1], MOD - 2, MOD)
    % MOD
)

answer = (2 * comb - n) % MOD

print(answer)