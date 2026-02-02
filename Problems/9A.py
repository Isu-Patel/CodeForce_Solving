import math

Y, W = map(int, input().split())

m = max(Y, W)

numerator = 7 - m
denominator = 6

g = math.gcd(numerator, denominator)

numerator //= g
denominator //= g

print(f"{numerator}/{denominator}")