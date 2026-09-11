import sys

input = sys.stdin.readline

N, K = map(int, input().split())

data = list(map(int, input().split()))
C = data[0]
holidays = data[1:]

last = 0
ans = 0

for day in holidays:
    while day - last > K:
        last += K
        ans += 1

    last = day
    ans += 1

while N - last > K:
    last += K

print(ans)