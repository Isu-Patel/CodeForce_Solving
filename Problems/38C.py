n, l = map(int, input().split())
a = list(map(int, input().split()))

mx = max(a)
ans = 0

for d in range(l, max + 1):
    pieces = 0
    for x in a:
        pieces += x // d
    ans = max(ans, pieces * d)

print(ans)
