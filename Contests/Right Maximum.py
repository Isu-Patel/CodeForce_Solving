import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ops = 0
    while a:
        # Find rightmost maximum
        max_val = max(a)
        rightmost_max_idx = -1
        for i in range(len(a) - 1, -1, -1):
            if a[i] == max_val:
                rightmost_max_idx = i
                break
        
        # Remove from rightmost_max_idx onwards
        a = a[:rightmost_max_idx]
        ops += 1
    
    print(ops)
