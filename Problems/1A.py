# import sys
# n = list[map(int, input().split(" "))]

# x, y = 0, 0
# if n[0]%n[2] == 0:
#    x = n[0]//n[2]
# else:
#    x = n[0]//n[2] + 1

# if n[1]%n[2] == 0:
#    y = n[1]//n[2]
# else:
#    y = n[1]//n[2] + 1

# print(x * y)

import sys
import math

input = sys.stdin.readline

n, m, a = map(int, input().split())

length_needed = (n + a - 1) // a
width_needed = (m + a - 1) // a

total_flagstones = length_needed * width_needed

print(total_flagstones)
