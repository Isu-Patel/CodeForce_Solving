n, d, m, l = map(int, input().split())

x = 0

while True:
    x += d
    if x % m > l:
        print(x)
        break