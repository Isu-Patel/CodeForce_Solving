# Hello Myself Isu Patel. I solve CodeForce problems and submit on github for people for easy to check code.
# This is Code is written by me only.
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    ans = []

    for start in range(n):
        cur = 0
        mn = 10 ** 18

        for step in range(1, n):
            edge = (start + step - 1) % n
            mn = min(mn, h[edge])
            cur += mn

        ans.append(cur)

    print(*ans)