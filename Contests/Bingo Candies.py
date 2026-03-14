import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    cnt = Counter()
    
    for _ in range(n):
        row = list(map(int, input().split()))
        for x in row:
            cnt[x] += 1
    
    limit = n * (n - 1)
    
    ok = True
    for v in cnt.values():
        if v > limit:
            ok = False
            break
    
    print("YES" if ok else "NO")