n = int(input())
a = set(map(int, input().split()))

x = 1

while x in a:
    x += 1

print(x)