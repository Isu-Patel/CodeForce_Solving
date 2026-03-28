from collections import deque

n, k = map(int, input().split())
h = list(map(int, input().split()))

max_len = 0
periods = []

# Try each starting position
for i in range(n):
    min_h = h[i]
    max_h = h[i]
    
    for j in range(i, n):
        min_h = min(min_h, h[j])
        max_h = max(max_h, h[j])
        
        if max_h - min_h <= k:
            length = j - i + 1
            if length > max_len:
                max_len = length
                periods = [(i + 1, j + 1)]  # 1-indexed
            elif length == max_len:
                periods.append((i + 1, j + 1))
        else:
            break  # Can't extend further from this start

print(max_len, len(periods))
for start, end in periods:
    print(start, end)
