a, b, c, d, e, f = map(int, input().split())

ron = c == 0 and d > 0

if d > 0 and b > 0 and (a == 0 or (e == 0 and f > 0)):
    ron = True

if a > 0 and c > 0 and e > 0 and b * d * f > a * c * e:
    ron = True

print("Ron" if ron else "Hermione")