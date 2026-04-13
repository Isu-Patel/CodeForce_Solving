
import sys
input = sys.stdin.readline

n = int(input())

a = [list(map(float, input().split())) for _ in range(n)]

N = 1 << n
dp = [0.0] * N

# all fish alive initially
dp[(1 << n) - 1] = 1.0

for mask in range((1 << n) - 1, 0, -1):
    k = bin(mask).count('1')
    if k <= 1:
        continue
    
    total_pairs = k * (k - 1) / 2
    
    for i in range(n):
        if not (mask & (1 << i)):
            continue
        for j in range(i + 1, n):
            if not (mask & (1 << j)):
                continue
            
            # i eats j
            dp[mask ^ (1 << j)] += dp[mask] * a[i][j] / total_pairs
            
            # j eats i
            dp[mask ^ (1 << i)] += dp[mask] * a[j][i] / total_pairs

# output
for i in range(n):
    print(f"{dp[1 << i]:.6f}", end=" ")