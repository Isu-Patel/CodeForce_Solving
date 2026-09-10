import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []

for i in range(n):
    j = i
    while b[j] != a[i]:
        j += 1

    while j > i:
        b[j], b[j - 1] = b[j - 1], b[j]
        ans.append(j)
        j -= 1

print(len(ans))
for x in ans:
    print(x, x + 1)
    