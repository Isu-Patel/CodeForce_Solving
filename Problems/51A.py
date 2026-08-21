import sys

input = sys.stdin.readline

n = int(input())

shapes = set()

for _ in range(n):
    row1 = input().strip()
    row2 = input().strip()

    # Skip **
    input()

    a = row1[0]
    b = row1[1]
    c = row2[0]
    d = row2[1]

    r1 = a + b + c + d
    r2 = c + a + d + b
    r3 = d + c + b + a
    r4 = b + d + a + c

    shapes.add(min(r1, r2, r3, r4))

print(len(shapes))