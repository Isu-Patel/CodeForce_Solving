import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
parent = [-1] * n

best_len = 0
best_pos = -1

for i in range(n):
    if a[i] == 1:
        dp[i] = 1

    for j in range(i):
        if a[j] == a[i] - 1 and dp[j] > 0:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    if dp[i] > best_len:
        best_len = dp[i]
        best_pos = i

if best_len == 0:
    print(0)
else:
    ans = []
    cur = best_pos
    while cur != -1:
        ans.append(cur + 2001)
        cur = parent[cur]

    ans.reverse()
    print(best_len)
    print(*ans)