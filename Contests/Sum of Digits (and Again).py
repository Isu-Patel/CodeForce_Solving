import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)
    
    if n == 1:
        print(s)
        continue
    
    cnt = Counter(s)
    total = sum(int(c) for c in s)
    
    # Try each possible digit sum efficiently
    # Start from reasonable range
    found = False
    
    for ds in range(1, min(total + 1, 9 * n + 1)):
        # Build suffix
        chain = []
        cur = ds
        
        while cur > 9:
            chain.append(str(cur))
            cur = sum(int(d) for d in str(cur))
        chain.append(str(cur))
        
        suffix = ''.join(chain)
        
        if len(suffix) >= n:
            continue
        
        # Quick check: suffix digits subset of s
        cnt_suf = Counter(suffix)
        if not all(cnt_suf[c] <= cnt[c] for c in cnt_suf):
            continue
        
        # Remaining digits
        temp = cnt.copy()
        for c in cnt_suf:
            temp[c] -= cnt_suf[c]
        
        # Check sum
        if sum(int(c) * f for c, f in temp.items()) != ds:
            continue
        
        # Build result
        first = []
        for d in '9876543210':
            first.extend([d] * temp[d])
        
        if first[0] == '0':
            for i in range(1, len(first)):
                if first[i] != '0':
                    first[0], first[i] = first[i], first[0]
                    break
        
        print(''.join(first) + suffix)
        found = True
        break
    
    if not found:
        print(s)
