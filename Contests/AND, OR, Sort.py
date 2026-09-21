# Hi! I am Isu Patel. I submit codeforce competition solutions.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    pref1 = [0] * (n + 1)

    for i in range(n):
        pref1[i + 1] = pref1[i] + (s[i] == '1')

    total_ones = pref1[n]

    ans = n

    for i in range(n + 1):
        if i > 0 and s[0] != '0':
            continue

        if i == 0 and s[0] != '1':
            continue

        left_cost = pref1[i]

        right_ones = total_ones - pref1[i]
        right_len = n - i
        right_cost = right_len - right_ones

        ans = min(ans, left_cost + right_cost)

    print(ans)