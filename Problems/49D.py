n = int(input())
s = input().strip()

ans = 0
i = 0

while i < n:
    j = i

    while j < n and s[j] == s[i]:
        j += 1

    length = j - i

    if length > 1:
        ans += length // 2

    i = j

print(ans)
