import sys
from heapq import heappush, heappop

MOD = 998244353

def modinv(a):
    return pow(a, MOD - 2, MOD)

def msf(arr, k):
    fracs = [[1, x] for x in arr]
    
    for _ in range(k):
        best_idx = -1
        best_gain = 0
        best_op = 0
        
        for i in range(len(fracs)):
            num, denom = fracs[i]
            
            # Try numerator increase
            gain1 = modinv(denom)
            if gain1 > best_gain:
                best_gain = gain1
                best_idx = i
                best_op = 0
            
            # Try denominator decrease
            if denom > 1:
                gain2 = (num * modinv(denom - 1) - num * modinv(denom) + MOD) % MOD
                if gain2 > best_gain:
                    best_gain = gain2
                    best_idx = i
                    best_op = 1
        
        if best_idx >= 0:
            if best_op == 0:
                fracs[best_idx][0] += 1
            else:
                fracs[best_idx][1] -= 1
    
    return sum(num * modinv(denom) for num, denom in fracs) % MOD

n, m = map(int, input().split())
a = list(map(int, input().split()))
k_arr = list(map(int, input().split()))

for k in k_arr:
    ans = 0
    for l in range(n):
        for r in range(l, n):
            ans += msf(a[l:r+1], k)
            ans %= MOD
    print(ans)
