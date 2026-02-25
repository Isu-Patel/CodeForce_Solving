import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s, m = map(int, input().split())
    
    # If s has bits not in m → impossible
    if s & (~m):
        print(-1)
        continue
    
    # Special case m = 0
    if m == 0:
        if s == 0:
            print(1)
        else:
            print(-1)
        continue
    
    # Minimum number of elements
    # ceil(s / m)
    n = (s + m - 1) // m
    print(n)