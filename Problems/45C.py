import sys
import heapq

input = sys.stdin.readline

n = int(input())
gender = input().strip()
a = list(map(int, input().split()))

left = [i - 1 for i in range(n)]
right = [i + 1 for i in range(n)]
right[n - 1] = -1

alive = [True] * n

heap = []

for i in range(n - 1):
    if gender[i] != gender[i + 1]:
        heapq.heappush(
            heap,
            (abs(a[i] - a[i + 1]), i, i + 1)
        )
ans = []

while heap:
    diff, u, v = heapq.heappop(heap)

    if not alive[u] or not alive[v]:
        continue

    if right[u] != v:
        continue

    ans.append((u + 1, v + 1))

    L = left[u]
    R = right[v]

    alive[u] = False
    alive[v] = False

    if L != -1:
        right[L] = R

    if R != -1:
        left[R] = L

    if L != -1 and R != -1 and gender[L] != gender[R]:
        heapq.heappush(
            heap,
            (abs(a[L] - a[R]), L, R)
        )

print(len(ans))

for u, v in ans:
    print(u, v)