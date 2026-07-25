n = int(input())

used = set()
ans = []

for _ in range(n):
    l, r = map(int, input().split())

    day = l

    while day in used:
        day += 1

    used.add(day)
    ans.append(day)

print(*ans)
