n = int(input())
a = list(map(int, input().split()))

ans = 1

for i in range(n):
    count = 1

    j = i - 1
    while j >= 0 and a[j] <= a[j]:
        count += 1
        j -= 1

    j = i + 1

    while j < n and a[j] <= a[j - 1]:
        count += 1
        j += 1

    ans = max(ans, count)

print(ans)