import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

MAX = max(a)

cnt = [0] * (MAX + 2)

for x in a:
    cnt[x] += 1

for x in range(1, MAX + 1):
    if cnt[x] < cnt[x + 1]:
        print(-1)
        sys.exit()

groups = cnt[1]

ans = [0] * n

positions = [[] for _ in range(MAX + 1)]

for i, x in enumerate(a):
    positions[x].append(i)

for x in range(1, MAX + 1):
    for j, idx in enumerate(positions[x]):
        ans[idx] = j + 1

print(groups)
print(*ans)