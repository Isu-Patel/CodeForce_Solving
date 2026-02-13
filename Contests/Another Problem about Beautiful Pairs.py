import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(n):
        ai = a[i]
        
        # iterate multiples of ai
        k = ai
        while i + k < n:
            j = i + k
            if ai * a[j] == j - i:
                ans += 1
            k += ai
    
    print(ans)
