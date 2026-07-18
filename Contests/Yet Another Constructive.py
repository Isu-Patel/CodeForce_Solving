# Hi this is second question of CodeForce Solution
# Check the soluition on github.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, m = map(int, input().split())

    if m < k:
        print("NO")
        continue

    print("YES")

    pref = [0] * (n + 1)

    for i in range(1, min(k, n) + 1):
        if i < k:
            pref[i] = i
        else:
            pref[i] = 0

    for i in range(k + 1, n + 1):
        pref[i] = (i - k) % k

    ans = []
    for i in range(1, n + 1):
        x = (pref[i] - pref[i - 1]) % m
        if x == 0:
            x = m
        ans.append(x)

    print(*ans)