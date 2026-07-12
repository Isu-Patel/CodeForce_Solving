t = int(input())

for _ in range(t):
    n = int(input())

    ans = [0] * n
    evens = list(range(2, n + 1, 2))
    odds = list(range(1, n + 1, 2))

    e = o = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            ans[i - 1] = evens[e]
            e += 1
        else:
            ans[i - 1] = odds[o]
            o += 1

    print(*ans)