import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    strips = [input().strip() for _ in range(k)]
    
    # possible[i] = set of letters at column i
    possible = [set() for _ in range(n)]
    
    for s in strips:
        for i in range(n):
            possible[i].add(s[i])
    
    # find divisors of n
    divisors = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            divisors.append(d)
            if d != n // d:
                divisors.append(n // d)
    
    divisors.sort()
    
    answer = None
    
    for d in divisors:
        ok = True
        pattern = [''] * d
        
        for r in range(d):
            common = possible[r].copy()
            
            for pos in range(r, n, d):
                common &= possible[pos]
                if not common:
                    ok = False
                    break
            
            if not ok:
                break
            
            pattern[r] = next(iter(common))
        
        if ok:
            answer = ''.join(pattern) * (n // d)
            break
    
    print(answer)
