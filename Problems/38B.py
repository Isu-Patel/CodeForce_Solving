rook = input().strip()
knight = input().strip()

def pos(s):
    return ord(s[0]) - ord('a'), int(s[1]) - 1

rx, ry = pos(rook)
kx, ky = pos(knight)

moves = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

ans = 0

for x in range(8):
    for y in range(8):
        if (x, y) == (rx, ry) or (x, y) == (kx, ky):
            continue
            
        if x == rx or y == ry:
            continue

        attacked = False
        for dx, dy in moves:
            if (kx + dx, ky + dy) == (x, y):
                attacked = True
                break
        
        if attacked:
            continue

        bad = False
        for dx, dy in moves:
            if (x + dx, y + dy) == (rx, ry):
                bad = True
                break
            if (x + dx, y + dy) == (kx, ky):
                bad = True
                break
        
        if bad:
            continue

        ans += 1

print(ans)