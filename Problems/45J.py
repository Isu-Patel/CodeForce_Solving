n, m = map(int, input().split())

# One-dimensional case
if n == 1 or m == 1:
    L = max(n, m)
    if L == 1:
        print(1)
    elif L <= 3:
        print(-1)
    else:
        seq = list(range(2, L + 1, 2)) + list(range(1, L + 1, 2))
        if n == 1:
            print(*seq)
        else:
            for x in seq:
                print(x)
    exit()

# Impossible
if n == 2 and m == 2:
    print(-1)
    exit()

# Transpose if needed (construction assumes m >= n)
rev = False
if n > m:
    n, m = m, n
    rev = True

# Special order for columns
if m == 2:
    col = [1, 2]
elif m == 3:
    col = [1, 3, 2]
else:
    col = list(range(2, m + 1, 2)) + list(range(1, m + 1, 2))

# Special order for rows
if n == 2:
    row = [1, 2]
elif n == 3:
    row = [1, 3, 2]
else:
    row = list(range(2, n + 1, 2)) + list(range(1, n + 1, 2))

ans = [[0] * m for _ in range(n)]

cur = 1
for r in row:
    for c in col:
        ans[r - 1][c - 1] = cur
        cur += 1

if rev:
    out = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            out[j][i] = ans[i][j]
    for row in out:
        print(*row)
else:
    for row in ans:
        print(*row)