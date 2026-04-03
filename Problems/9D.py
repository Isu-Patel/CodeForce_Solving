n, h = map(int, input().split())

# dp[n][h] = number of BSTs with n nodes and height <= h
dp = [[0] * (n + 1) for _ in range(n + 1)]

# Base case: empty tree
for i in range(n + 1):
    dp[0][i] = 1

# Fill DP table
for height in range(1, n + 1):
    for nodes in range(1, n + 1):
        total = 0
        for root in range(1, nodes + 1):
            total += dp[root - 1][height - 1] * dp[nodes - root][height - 1]
        dp[nodes][height] = total

# Catalan numbers
catalan = [0] * (n + 1)
catalan[0] = 1

for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        total += catalan[j - 1] * catalan[i - j]
    catalan[i] = total

# Final answer
answer = catalan[n] - dp[n][h - 1]
print(answer)