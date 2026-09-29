import sys

k = int(input())
s = list(input().strip())

n = len(s)

for i in range(n // 2):
    j = n - 1 - i

    if s[i] != '?' and s[j] != '?' and s[i] != s[j]:
        print("IMPOSSIBLE")
        sys.exit()

    if s[i] == '?':
        s[i] = s[j]
    elif s[j] == '?':
        s[j] = s[i]

if n % 2 == 1 and s[n // 2] == '?':
    s[n // 2] = 'a'

present = set(s)

missing = []
for i in range(k):
    ch = chr(ord('a') + i)
    if ch not in present:
        missing.append(ch)

original = input if False else None