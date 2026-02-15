import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    
    # make 1-indexed
    f = [0] + f
    
    # g[x] = f[x+1] - f[x]
    g = [0]*(n+1)
    for i in range(1, n):
        g[i] = f[i+1] - f[i]
    
    a = [0]*(n+1)
    
    # compute a[2..n] using second difference
    for i in range(2, n+1):
        a[i] = (g[i-1] - g[i-2]) // 2
    
    # compute a[1] using f(1)
    # f(1) = sum(a[i]*(i-1))
    sum_known = 0
    for i in range(2, n+1):
        sum_known += a[i] * (i-1)
    
    a[1] = f[1] - sum_known
    
    print(*a[1:])
