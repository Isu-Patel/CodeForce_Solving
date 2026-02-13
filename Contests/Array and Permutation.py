import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i
    
    prev = -1
    possible = True
    
    for i in range(n):
        current = pos[a[i]]
        if current < prev:
            possible = False
            break
        prev = current
    
    print("YES" if possible else "NO")