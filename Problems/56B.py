import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

l = 0
while l < n and a[l] == l + 1:
    l += 1

if l == n:
    print(0, 0)
    sys.exit()

r = n - 1
while r >= 0 and a[r] == r + 1:
    r -= 1

a[l:r + 1] = reversed(a[l:r + 1])

for i in range(n):
    if a[i] != i + 1:
        print(0, 0)
        sys.exit()

print(l + 1, r + 1)