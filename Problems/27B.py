n = int(input())

played = set()
wins = [0] * (n + 1)

m = n * (n - 1) // 2 - 1

for _ in range(m):
    x, y = map(int, input().split())

    played.add((x, y))
    wins[x] += 1

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):

        if (i, j) not in played and (j, i) not in played:

            if wins[i] > wins[j]:
                print(i, j)
            else:
                print(j, i)

            
            exit()