s = input().strip()

upper = sum(1 for ch in s if ch.isupper())

if upper > len(s) - upper:
    print(s.upper())
else:
    print(s.lower())