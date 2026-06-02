n = int(input())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r, i + 1))

intervals.sort()

if n == 1:
    print(1)
    print(1)
    exit()

bad = [0] * (n - 1)
total_bad = 0

for i in range(n - 1):
    if intervals[i][1] > intervals[i + 1][0]:
        bad[i] = 1
        total_bad += 1

ans = []

for k in range(n):
    outside = total_bad

    if k > 0:
        outside -= bad[k - 1]
    if k < n - 1:
        outside -= bad[k]

    if outside != 0:
        continue

    ok = True

    if 0 < k < n - 1:
        if intervals[k - 1][1] > intervals[k + 1][0]:
            ok = False
    
    if ok:
        ans.append(intervals[k][2])

ans.sort()

print(len(ans))
if ans:
    print(*ans)