n = int(input())
a = list(map(int, input().split()))

pos = []
neg = []
zeros = []

for x in a:
    if x > 0:
        pos.append(x)
    elif x < 0:
        neg.append(x)
    else:
        zeros.append(x)

neg.sort()

ans = []

ans.extend(pos)

if len(neg) % 2 == 0:
    ans.extend(neg)
else:
    if len(neg) > 1:
        ans.extend(neg[:-1])

if ans:
    print(*ans)
else:
    if zeros:
        print(0)
    else:
        print(neg[-1])
        