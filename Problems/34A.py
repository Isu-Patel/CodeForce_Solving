n = int(input())
a = list(map(int, input().split()))

best_diff = abs(a[0] - a[-1])
ans_i, ans_j = n, 1

for i in range(n - 1):
    diff = abs(a[i] - a[i + 1])

    if diff < best_diff:
        best_diff = diff
        ans_i = i + 1
        ans_j = i + 2

print(ans_i, ans_j)
