import math

a, b, x, y = map(int, input().split())

g = math.gcd(x, y)
x //= g
y //= g

k = min(a // x, b // y)

if k == 0:
    print(0, 0)
else:
    print(k * x, k * y)