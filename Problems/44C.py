n, m = map(int, input().split())

cnt = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    for day in range(a, b + 1):
        cnt[day] += 1

for day in range(1, n + 1):
    if cnt[day] != 1:
        print(day, cnt[day])
        break

else:
    print("OK")