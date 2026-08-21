n = int(input())

shapes = set()

for _ in range(n):
    row1 = input().strip()
    row2 = input().strip()

    input()

    a = row1[0]
    b = row1[1]
    c = row2[0]
    d = row2[1]

    rotations = [
        a + b + c + d,
        c + a + d + b,
        d + c + b + a,
        b + d + a + c
    ]

    shapes.add(min(rotations))

print(len(shapes))
