import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().strip()
    digits = list(map(int, s))
    
    n = len(digits)
    
    # try all target sums 1..9
    ans = n
    
    for target in range(1, 10):
        # DP-like greedy
        temp = sorted(digits)
        total = 0
        keep = 0
        
        for d in temp:
            if total + d <= target:
                total += d
                keep += 1
            else:
                break
        
        ans = min(ans, n - keep)
    
    print(ans)