import sys

input = sys.stdin.readline


def digit_sum(n):
   return sum(int(d) for d in str(n))

t = int(input())

for _ in range(t):
   x = int(input())

   count = 0

   for s in range(1, 91):
      y = x + s
      if digit_sum(y) == s:
         count += 1

   print(count)