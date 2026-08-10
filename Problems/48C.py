from fractions import Fraction

n = int(input())
s = list(map(int, input().split()))


L = Fraction(10, 1)
R = None

for i in range(n):
    idx = i + 1

    low = Fraction(10 * s[i], idx)
    high = Fraction(10 * (s[i] + 1), idx)

    L = max(L, low)

    if R is None:
        R = high
    else:
        R = min(R, high)


QL = Fraction(n + 1, 10) * L
QR = Fraction(n + 1, 10) * R

min_next = QL.numerator // QL.denominator

max_next = (QR.numerator + QR.denominator - 1) // QR.denominator - 1

if min_next == max_next:
    print("unique")
    print(min_next)
else:
    print("not unique")