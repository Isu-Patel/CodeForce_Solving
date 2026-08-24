n = int(input())
a = list(map(int, input().split()))

cnt = [0, 0, 0, 0]

for x in a:
    cnt[x] += 1

print(n - max(cnt[1], cnt[2], cnt[3]))
