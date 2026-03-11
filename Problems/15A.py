n, t = map(int, input().split())

houses = []
for _ in range(n):
    x, a = map(int, input().split())
    houses.append((x, a))

houses.sort()

ans = 2

for i in range(n - 1):
    x1, a1 = houses[i]
    x2, a2 = houses[i+1]
    
    gap = x2 - x1 - (a1 + a2) / 2
    
    if gap > t:
        ans += 2
    elif gap == t:
        ans += 1

print(ans)