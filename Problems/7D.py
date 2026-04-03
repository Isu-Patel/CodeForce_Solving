import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

# Rolling hash parameters
base = 131
mod = 10**9 + 7

# Precompute powers
pow_base = [1] * (n + 1)
for i in range(1, n + 1):
    pow_base[i] = pow_base[i-1] * base % mod

# Forward and reverse hash
h_forward = [0] * (n + 1)
h_reverse = [0] * (n + 1)

for i in range(n):
    h_forward[i+1] = (h_forward[i] * base + ord(s[i])) % mod
    h_reverse[i+1] = (h_reverse[i] * base + ord(s[n-1-i])) % mod

def get_hash(h, l, r):
    return (h[r] - h[l] * pow_base[r-l]) % mod

deg = [0] * n
answer = 0

for i in range(n):
    # check if s[0..i] is palindrome
    left_hash = get_hash(h_forward, 0, i+1)
    right_hash = get_hash(h_reverse, n-1-i, n)
    
    if left_hash == right_hash:
        if i == 0:
            deg[i] = 1
        else:
            deg[i] = 1 + deg[(i-1)//2]
    else:
        deg[i] = 0
    
    answer += deg[i]

print(answer)