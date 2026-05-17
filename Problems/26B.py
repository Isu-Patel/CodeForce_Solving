import sys
s = sys.stdin.readline().strip()
open_count = 0
ans = 0
for ch in s:
    if ch == '(':
        open_count += 1
    elif open_count > 0:
        open_count -= 1
        ans += 2

print(ans)