import sys
import math

input = sys.stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))
C = data[0]
holidays = data[1:]

last = 0
ans = 0

for day in holidays:
    gap = day - last

    ans += (gap + K - 1) // K - 1

    ans += 1
    last = day

ans += (N - last) // K

print(ans)