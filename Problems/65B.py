
import sys

input = sys.stdin.readline

n = int(input())
prev = 1000
ans = []

for _ in range(n):
    s = input().strip()
    candidates = []

    for year in range(1000, 2012):
        t = str(year)

        diff = sum(a != b for a, b in zip(s, t))

        if diff <= 1 and year >= prev:
            candidates.append(year)

    if not candidates:
        print("No solution")
        sys.exit()

    chosen = min(candidates)
    ans.append(chosen)
    prev = chosen

print(*ans, sep="\n")
