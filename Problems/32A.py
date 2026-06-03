n, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(i + 1, n):
        if abs(a[i] - a[j]) <= d:
            ans += 2

print(ans)