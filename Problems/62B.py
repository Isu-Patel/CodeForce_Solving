import sys
from bisect import bisect_left

input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip()

positions = [[] for _ in range(26)]

for i, ch in enumerate(s):
    positions[ord(ch) - ord('a')].append(i)

for _ in range(n):
    c = input().strip()
    ans = 0
    m = len(c)

    for i, ch in enumerate(c):
        arr = positions[ord(ch) - ord('a')]

        if not arr:
            ans += m
            continue

        idx = bisect_left(arr, i)

        best = float('inf')

        if idx < len(arr):
            best = arr[idx] - i

        if idx > 0:
            best = min(best, i - arr[idx - 1])

        ans += best

    print(ans)