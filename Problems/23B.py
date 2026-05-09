import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
for _ in range(t):
    n = int(data[index])
    index += 1
    if n == 1:
        print(1)
    elif n == 2:
        print(0)
    else:
        print(n - 2)