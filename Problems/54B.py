import sys

input = sys.stdin.readline

A, B = map(int, input().split())
g = [input().strip() for _ in range(A)]


def rotate(piece):
    h = len(piece)
    w = len(piece[0])

    return [
        ''.join(piece[h - 1 - r][c] for r in range(h))
        for c in range(w)
    ]


def canonical(piece):
    forms = []

    cur = piece

    for _ in range(4):
        forms.append('|'.join(cur))
        cur = rotate(cur)

    return min(forms)


def good(X, Y):
    seen = set()

    for r in range(0, A, X):
        for c in range(0, B, Y):
            piece = [
                g[i][c:c + Y]
                for i in range(r, r + X)
            ]

            key = canonical(piece)

            if key in seen:
                return False

            seen.add(key)

    return True


count = 0
best = None

for X in range(1, A + 1):
    if A % X != 0:
        continue

    for Y in range(1, B + 1):
        if B % Y != 0:
            continue

        if good(X, Y):
            count += 1

            if best is None:
                best = (X, Y)
            else:
                area = X * Y
                best_area = best[0] * best[1]

                if area < best_area or (
                    area == best_area and X < best[0]
                ):
                    best = (X, Y)

print(count)
print(best[0], best[1])