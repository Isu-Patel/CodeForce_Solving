import math

x, y = map(int, input().split())

d2 = x * x + y * y
d = math.isqrt(d2)

# Points on circles of integer radius are black
if d * d == d2:
    print("black")
else:
    if x >= 0:
        if d % 2 == 0:
            print("black")
        else:
            print("white")
    else:
        if d % 2 == 0:
            print("white")
        else:
            print("black")