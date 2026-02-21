import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, h, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # prefix sums
    pref = [0]*n
    pref[0] = a[0]
    for i in range(1, n):
        pref[i] = pref[i-1] + a[i]
    
    total = pref[-1]
    
    # number of full magazines before last partial
    cycles = (h - 1) // total
    remaining = h - cycles * total
    
    # time spent in full magazines + reloads
    base_time = cycles*n + cycles*k
    
    # suffix max values
    sufmax = [0]*(n+1)
    for i in range(n-1, -1, -1):
        sufmax[i] = max(sufmax[i+1], a[i])
    
    # best improvement if swap at position i
    best_diff = [0]*n
    for i in range(n-1):
        best_diff[i] = max(0, sufmax[i+1] - a[i])
    
    # prefix maximum of gains
    pref_best = [0]*n
    pref_best[0] = best_diff[0]
    for i in range(1, n):
        pref_best[i] = max(pref_best[i-1], best_diff[i])
    
    shots = n  # worst
    
    for tpos in range(n):
        # no swap
        if pref[tpos] >= remaining:
            shots = min(shots, tpos+1)
        
        # with one swap
        if pref[tpos] + pref_best[tpos] >= remaining:
            shots = min(shots, tpos+1)
    
    print(base_time + shots)