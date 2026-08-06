from itertools import permutations

conds = [input().strip() for _ in range(3)]

for p in permutations("ABC"):
    pos = {p[i]: i for i in range(3)}
    ok = True

    for s in conds:
        x, op, y = s[0], s[1], s[2]
        if op == "<":
            if pos[x] >= pos[y]:
                ok = False
                break
        else:
            if pos[x] <= pos[y]:
                ok = False
                break

    if ok:
        print("".join(p))
        break
else:
    print("Impossible")