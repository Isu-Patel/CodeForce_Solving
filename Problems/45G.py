import math

n = int(input())

S = n * (n + 1) // 2

limit = math.isqrt(S) + 1

is_small_prime = [True] * (limit + 1)
is_small_prime[0] = is_small_prime[1] = False

primes = []

for i in range(2, limit + 1):
    if is_small_prime[i]:
        primes.append(i)

        if i * i <= limit:
            for j in range(i * i, limit + 1, i):
                is_small_prime[j] = False

def is_prime(x):
    if x < 2:
        return False

    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            return False


    return True

ans = [1] * (n + 1)

if is_prime(S):
    print(*ans[1:])
    exit()


if S % 2 == 0:
    for p in range(2, n + 1):
        if is_prime(p) and is_prime(S - p):
            ans[p] = 2
            print(*ans[1:])
            exit()

else:

    if n >= 2 and is_prime(S - 2):
        ans[2] = 2
        print(*ans[1:])
        exit()


    for p in range(2, n + 1):

        if p == 3:
            continue

        if is_prime(p) and is_prime(S - 3 - p):
            ans[3] = 2
            ans[p] = 3

            print(*ans[1:])
            exit()


print(-1)
