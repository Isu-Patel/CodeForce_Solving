n, m, s = map(int, input().split())

qn = n // s
rn = n % s

if rn > 0:
    rows = rn * (qn + 1)
else:
    rows = n

qm = m // s
rm = m % s

if rm > 0:
    cols = rm * (qm + 1)
else:
    cols = m

print(rows * cols)