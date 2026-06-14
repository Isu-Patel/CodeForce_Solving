n = int(input())
a = list(map(int, input().split()))

total = sum(a)

cur = a[0]
best = a[0]

for x in a[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)

print(-total + 2 * max*(0, best))