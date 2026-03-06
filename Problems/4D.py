import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())

env = []
for i in range(1, n+1):
    wi, hi = map(int, input().split())
    if wi > w and hi > h:
        env.append((wi, hi, i))

# if no envelope fits
if not env:
    print(0)
    exit()

# sort by width then height
env.sort()

m = len(env)

dp = [1]*m
parent = [-1]*m

best = 0
best_idx = 0

for i in range(m):
    for j in range(i):
        if env[j][0] < env[i][0] and env[j][1] < env[i][1]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    if dp[i] > best:
        best = dp[i]
        best_idx = i

print(best)

# reconstruct chain
res = []
cur = best_idx

while cur != -1:
    res.append(env[cur][2])
    cur = parent[cur]

res.reverse()

print(*res)