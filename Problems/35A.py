pos = int(input())

for _ in range(3):
    a, b = map(int, input().split())

    if pos == a:
        pos = b
    elif pos == b:
        pos = a

print(pos)
