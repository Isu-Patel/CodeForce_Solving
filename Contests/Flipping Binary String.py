import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ones = s.count('1')
    zeros = n - ones
    
    # Strategy 1: choose all '1'
    if ones % 2 == 0:
        ops = [i+1 for i in range(n) if s[i] == '1']
        print(len(ops))
        if ops:
            print(*ops)
        else:
            print()
    
    # Strategy 2: choose all '0'
    elif zeros % 2 == 1:
        ops = [i+1 for i in range(n) if s[i] == '0']
        print(len(ops))
        print(*ops)
    
    else:
        print(-1)