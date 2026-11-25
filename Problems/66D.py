n = int(input())

if n == 2:
    print(-1)
else:
    print(6)
    print(10)
    print(15)
    for i in range(1, n - 2):
        print(30 ** i)