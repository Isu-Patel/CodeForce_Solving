n = int(input())
s = input().strip()
res = []
i = 0

if n % 2 == 1:
    res.append(s[:3])
    i = 3
while i < n:
    res.append(s[i:i + 2])
    i += 2

print('-'.join(res))
