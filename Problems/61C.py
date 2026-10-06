import sys

input = sys.stdin.readline

a, b = input().split()
a = int(a)

s = input().strip()


value = 0

for ch in s:
    if '0' <= ch <= '9':
        digit = ord(ch) - ord('0')
    else:
        digit = ord(ch) - ord('A') + 10

    value = value * a + digit


def to_roman(x):
    vals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    ans = []

    for v, symbol in vals:
        if x >= v:
            count = x // v
            ans.append(symbol * count)
            x %= v

    return ''.join(ans)


if b == 'R':
    print(to_roman(value))
else:
    base = int(b)

    if value == 0:
        print(0)
    else:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXY"
        ans = []

        while value > 0:
            ans.append(digits[value % base])
            value //= base

        print(''.join(reversed(ans)))