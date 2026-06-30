import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

marbles = []
for _ in range(n):
    x, c = map(int, input().split())
    marbles.sort((x, c))

marbles.sort()

x = [p[0] for p in marbles]
c = [p[1] for p in marbles]

INF = 10 ** 30

dp = [0] * n
for last in range(n):
    dp[last] = 0

for i in range(n - 1, 0, -1):
    ndp = [0] * n
    for last in range(i):
        pin = c[i] + dp[i]
        roll = (x[i] - x[last]) + dp[last]
        ndp[last] = min(pin, roll)
    dp = ndp

print(c[0] + dp[0])
