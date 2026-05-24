n = int(input())

camels = {}

for _ in range(n):
    x, d = map(int, input().split())
    camels[x] = x + d

for x in camels:
    y = camels[x]

    if y in camels:

        if camels[y] == x:
            print("YES")
            break

else:
    print("NO")