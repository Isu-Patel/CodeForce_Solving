# Myself Isu Patel. I solve CodeForce problems and submit on github for people for easy to check code.
t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    b.sort(reverse=True)

    if n == 2:
        print(b[0], b[1])
        continue

    ok = True

    for i in range(2, n):
        if b[i] != b[i - 2] % b[i - 1]:
            ok = False
            break

    if ok:
        print(b[0], b[1])
    else:
        print(-1)