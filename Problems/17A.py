n, k = map(int, input().split())

# Sieve
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

# list of primes
primes = [i for i in range(2, n+1) if is_prime[i]]

count = 0

# check condition
for i in range(len(primes) - 1):
    x = primes[i] + primes[i+1] + 1
    if x <= n and is_prime[x]:
        count += 1

print("YES" if count >= k else "NO")