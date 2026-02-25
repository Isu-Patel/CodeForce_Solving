import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, d = map(int, input().split())
    
    if m > d:
        print(n)
    else:
        h_max = d // m + 1
        # ceiling division
        towers = (n + h_max - 1) // h_max
        print(towers)