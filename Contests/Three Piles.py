# Hi myslef Isu Patel. I post asnwers of Coding Contest for Codeforecs.
# You can check out my Github Profile.

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    d = abs(a - b)

    print(max(d, c - d))