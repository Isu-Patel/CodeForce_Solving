import sys

input = sys.stdin.readline

n = int(input())

Lx = []
Rx = []
Ly = []
Ry = []
Cx = []
Cy = []
W = []


for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    lx, rx = sorted((x1, x2))
    ly, ry = sorted((y1, y2))

    side = rx - lx
    weight = side ** 3

    Lx.append(lx)
    Rx.append(rx)
    Ly.append(ly)
    Ry.append(ry)

    Cx.append((lx + rx) / 2.0)
    Cy.append((ly + ry) / 2.0)
    W.append(weight)

EPS = 1e-9

for k in range(1, n + 1):
    # Suffix center of mass
    sw = [0.0] * (k + 1)
    sx = [0.0] * (k + 1)
    sy = [0.0] * (k + 1)

    for i in range(k - 1, -1, -1):
        sw[i] = W[i] + (sw[i + 1] if i + 1 < k else 0)
        if i + 1 < k:
            sx[i] = (W[i] * Cx[i] + sw[i + 1] * sx[i + 1]) / sw[i]
            sy[i] = (W[i] * Cy[i] + sw[i + 1] * sy[i + 1]) / sw[i]
        else:
            sx[i] = Cx[i]
            sy[i] = Cy[i]

    stable = True

    # Check every interface
    for i in range(1, k):
        ox1 = max(Lx[i - 1], Lx[i])
        ox2 = min(Rx[i - 1], Rx[i])
        oy1 = max(Ly[i - 1], Ly[i])
        oy2 = min(Ry[i - 1], Ry[i])

        if (
            sx[i] < ox1 - EPS
            or sx[i] > ox2 + EPS
            or sy[i] < oy1 - EPS
            or sy[i] > oy2 + EPS
        ):
            stable = False
            break

    if not stable:
        print(k - 1)
        sys.exit()

print(n)