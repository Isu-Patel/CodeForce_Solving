import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

count = {}

for i in range(n):
    level = min(i, n - 1 - i)

    x = a[i] - level

    if x >= 1:
        count[x] = count.get(x, 0) + 1

best = max(count.values(), default=0)

print(n - best)