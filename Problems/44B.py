n, a, b, c = map(int, input().split())

ans = 0

for z in range(min(c, n) + 1):
    rem = 2 * n - 4 * z

    low = max(0, -((a - rem) // 2))
    high = min(b, rem // 2)

    if low <= high:
        ans += high - low + 1

print(ans)