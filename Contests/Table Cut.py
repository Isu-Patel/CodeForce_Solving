import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    pref = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            pref[i][j] = (
                grid[i-1][j-1]
                + pref[i-1][j]
                + pref[i][j-1]
                - pref[i-1][j-1]
            )
    
    S = pref[n][m]
    
    best = -1
    best_i, best_j = 1, 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            a = pref[i][j]
            value = a * (S - a)
            if value > best:
                best = value
                best_i, best_j = i, j
    
    print(best)
    
    # Construct path through best cell
    path = []
    
    # Go to (best_i, best_j)
    path += ['R'] * (best_j - 1)
    path += ['D'] * (best_i - 1)
    
    # Go to (n, m)
    path += ['D'] * (n - best_i)
    path += ['R'] * (m - best_j)
    
    print("".join(path))
