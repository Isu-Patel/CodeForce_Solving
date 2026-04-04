import sys

x = abs(int(sys.stdin.readline().strip()))

k = 0
S = 0

while S < x or (S - x) % 2 != 0:
    k += 1
    S += k

print(k)