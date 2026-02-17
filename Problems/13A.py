import math

A = int(input())

total_sum = 0

for base in range(2, A):
   x = A
   digit_sum = 0

   while x > 0:
      digit_sum += x % base
      x //= base

   total_sum += digit_sum

denominator = A - 2

g  = math.gcd(total_sum, denominator)

print(f"{total_sum // g}/{denominator // g}")