n = int(input())

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

LIMIT = 10 ** 18
ans = LIMIT

def dfs(idx, last_exp, divisors, value):
    global ans

    if divisors == n:
        ans = min(ans, value)
        return
    
    if divisors > n:
        return

    if idx >= len(primes):
        return
    
    p = primes[idx]
    cur = value

    for e in range(1, last_exp + 1):
        if cur > LIMIT // p:
            break
        cur *= p

        new_div = divisors * (e + 1)

        if n % new_div != 0:
            continue

        if cur >= ans:
            break

        dfs(idx + 1, e, new_div, cur)

dfs(0, 60, 1, 1)

print(ans)