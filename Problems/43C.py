n = int(input())
a = list(map(int, input().split()))

cnt = [0, 0, 0]

for x in a:
    cnt[x % 3] += 1

ans = cnt[0] // 2 + min(cnt[1], cnt[2])

print(ans)