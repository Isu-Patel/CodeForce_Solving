def pos(s):
    return (ord(s[0]) - ord('a'), int(s[1]) - 1)


tokens = input().split()
r1 = pos(tokens[0])
r2 = pos(tokens[1])
wk = pos(tokens[2])
bk = pos(tokens[3])


def rook_attacks(rook, target, occ):
    rx, ry = rook
    tx, ty = target

    if rx == tx:
        step = 1 if ty > ry else -1
        y = ry + step
        while y != ty:
            if (rx, y) in occ:
                return False
            y += step
        return True

    if ry == ty:
        step = 1 if tx > rx else -1
        x = rx + step
        while x != tx:
            if (x, ry) in occ:
                return False
            x += step
        return True

    return False


def attacked(square, rooks, wk, bk):
    if abs(square[0] - wk[0]) <= 1 and abs(square[1] - wk[1]) <= 1:
        return True

    occ = {wk, bk}
    for r in rooks:
        occ.add(r)

    for r in rooks:
        if rook_attacks(r, square, occ):
            return True
    return False


if not attacked(bk, [r1, r2], wk, bk):
    print("OTHER")
    exit()

dirs = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for dx, dy in dirs:
    nx = bk[0] + dx
    ny = bk[1] + dy

    if not (0 <= nx < 8 and 0 <= ny < 8):
        continue

    dest = (nx, ny)

    if dest == wk:
        continue

    if abs(nx - wk[0]) <= 1 and abs(ny - wk[1]) <= 1:
        continue

    rooks = []
    if r1 != dest:
        rooks.append(r1)
    if r2 != dest:
        rooks.append(r2)

    if not attacked(dest, rooks, wk, dest):
        print("OTHER")
        exit()

print("CHECKMATE")