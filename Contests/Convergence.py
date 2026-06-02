from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = n

    for x in set(a):
        left = 0
        right = 0

        for v in a:
            if v < x:
                left += 1
            elif v > x:
                right += 1

        ans = min(ans, max(left, right))

    print(ans)