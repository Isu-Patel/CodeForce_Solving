import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

vals = sorted(a)
rank = {v: i + 1 for i, v in enumerate(vals)}

bit = [0] * (n + 1)

def update(i):
    while i <= n:
        bit[i] += 1
        i += i & -i

def query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s

left = [0] * n

for i in range(n):
    r = rank[a[i]]
    left[i] = i - query(r)
    update(r)

bit = [0] * (n + 1)

answer = 0

for i in range(n - 1, -1, -1):
    r = rank[a[i]]
    right = query(r - 1)
    answer += left[i] * right
    update(r)

print(answer)