n = int(input())
a = list(map(int, input().split()))

for i in range(1, n - 1):

    if (a[i - 1] < a[i] > a[i + 1]) or (a[i - 1] > a[i] < a[i + 1]):
        print(3)
        print(i, i + 1, i + 2)

        break
else:
    print(0)