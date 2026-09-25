n = int(input())

ans = [n]

while n > 1:
    p = 2

    while p * p <= n and n % p != 0:
        p += 1

    n //= p
    ans.append(n)

print(*ans)