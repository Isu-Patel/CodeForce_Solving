import sys
from functools import lru_cache

data = ''.join(sys.stdin.read().split())

coords = []

rows = [
    (-2, range(0, 3)),
    (-1, range(-1, 3)),
    (0, range(-2, 3)),
    (1, range(-2, 2)),
    (2, range(-2, 1))
]

for r, qs in rows:
    for q in qs:
        coords.append((q, r))

groups = {}

for i, (q, r) in enumerate(coords):
    for key in (('r', r), ('q', q), ('s', q + r)):
        groups.setdefault(key, []).append(i)

moves = set()

for cells in groups.values():
    cells.sort(key=lambda i: coords[i])

    for l in range(len(cells)):
        mask = 0
        for j in range(l, len(cells)):
            mask |= 1 << cells[j]
            moves.add(mask)

by_high = [[] for _ in range(19)]

for move in moves:
    by_high[move.bit_length() - 1].append(move)

initial = 0

for i, ch in enumerate(data):
    if ch == 'O':
        initial |= 1 << i

@lru_cache(maxsize=None)
def grundy(mask):
    seen = 0

    bits = mask

    while bits:
        bit = bits & -bits
        bits -= bit

        i = bit.bit_length() - 1

        for move in by_high[i]:
            if mask & move == move:
                nxt = mask ^ move
                seen |= 1 << grundy(nxt)

    mex = 0
    while (seen >> mex) & 1:
        mex += 1

    return mex

if grundy(initial) == 0:
    print("Lillebror")
else:
    print("Karlsson")