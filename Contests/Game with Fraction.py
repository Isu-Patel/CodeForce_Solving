import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p, q = map(int, input().split())
    
    D = 3*p - 2*q
    
    if D >= 0 and D % 5 == 0:
        print("Bob")
    else:
        print("Alice")
