import sys
input = sys.stdin.readline

def f(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    else:
        return 0

n = int(input())

total = 0

for _ in range(n):
    x, m = map(int, input().split())
    L = x
    R = x + m - 1
    
    total ^= f(R) ^ f(L - 1)

if total != 0:
    print("tolik")
else:
    print("bolik")