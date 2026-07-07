import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = int(input())

need = x - 1
ans = 0

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if min(i, j, n - 1 - i, m - 1 - j) == need:
                ans += 1

print(ans)