import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

cover = [0] * (n + 2)
base = [0] * (n + 2)

for _ in range(m):
    a, b, c = map(int, input().split())

    cover[a] += 1
    cover[b + 1] -= 1

    v = c - a
    base[a] += v
    base[b + 1] -= v

for i in range(1, n + 1):
    cover[i] += cover[i - 1]
    base[i] += base[i - 1]

queries = list(map(int, input().split()))

answer = 0

for x in queries:
    answer += x * cover[x] + base[x]

print(answer)
