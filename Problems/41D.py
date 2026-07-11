import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
MOD = k + 1

board = [list(map(int, list(input().strip()))) for _ in range(n)]

NEG = -10**9

# dp[row][col][rem]
dp = [[[NEG] * MOD for _ in range(m)] for _ in range(n)]
par = [[[None] * MOD for _ in range(m)] for _ in range(n)]

# Base: bottom row
for c in range(m):
    val = board[n - 1][c]
    dp[n - 1][c][val % MOD] = val

# Process upwards
for r in range(n - 2, -1, -1):
    for c in range(m):
        val = board[r][c]
        for dc, move in [(-1, 'R'), (1, 'L')]:
            pc = c + dc
            if 0 <= pc < m:
                for rem in range(MOD):
                    if dp[r + 1][pc][rem] == NEG:
                        continue
                    new_sum = dp[r + 1][pc][rem] + val
                    new_rem = new_sum % MOD
                    if new_sum > dp[r][c][new_rem]:
                        dp[r][c][new_rem] = new_sum
                        par[r][c][new_rem] = (pc, rem, move)

# Find best in top row
best = NEG
start_col = -1

for c in range(m):
    if dp[0][c][0] > best:
        best = dp[0][c][0]
        start_col = c

if best == NEG:
    print(-1)
    sys.exit()

print(best)

# Reconstruct
moves = []
r = 0
c = start_col
rem = 0

while r < n - 1:
    pc, prem, mv = par[r][c][rem]
    moves.append(mv)
    c = pc
    rem = prem
    r += 1

# Bottom starting column
print(c + 1)
print("".join(reversed(moves)))