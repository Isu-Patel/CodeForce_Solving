n = int(input())

events = []

for i in range(n):
    l, r = map(int, input().split())
    events.append((r, l, i))

events.sort()

used = set()
ans = [0] * n

for r, l, idx in events:
    day = 1

    while day in used:
        day += 1

    ans[idx] = day
    used.add(day)

print(*ans)