n = int(input())
cnt = 0
for x in range(1, n + 1):
    d = 0
    t = x
    p = 2
    while p * p <= t:
        if t % p == 0:
            d += 1
            while t % p == 0:
                t //= p

        p += 1
    if t > 1:
        d += 1
    if d == 2:
        cnt += 1
print(cnt)