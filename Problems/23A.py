import sys

s = sys.stdin.read().strip()
n = len(s)
max_len = 0
for length in range(n, 0, -1):
    seen = set()
    for i in range(n - length + 1):
        sub = s[i:i + length]
        if sub in seen:
            max_len = length
            break
        seen.add(sub)
    if max_len > 0:
        break
print(max_len)

