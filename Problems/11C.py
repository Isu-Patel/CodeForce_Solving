import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [input().strip() for _ in range(n)]

    # Prefix sum
    ps = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            ps[i][j] = (a[i-1][j-1] == '1') + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

    def get(x1, y1, x2, y2):
        x1 = max(x1, 1)
        y1 = max(y1, 1)
        x2 = min(x2, n)
        y2 = min(y2, m)
        if x1 > x2 or y1 > y2:
            return 0
        return ps[x2][y2] - ps[x1-1][y2] - ps[x2][y1-1] + ps[x1-1][y1-1]

    ans = 0

    #Axis-aligned squares
    for i in range(1, n+1):
        for j in range(1, m+1):
            k = 2
            while i + k - 1 <= n and j + k - 1 <= m:
                x1, y1 = i, j
                x2, y2 = i + k - 1, j + k - 1

                border = (
                    get(x1, y1, x1, y2) +
                    get(x2, y1, x2, y2) +
                    get(x1+1, y1, x2-1, y1) +
                    get(x1+1, y2, x2-1, y2)
                )

                if border == 4*k - 4:
                    outer = get(x1-1, y1-1, x2+1, y2+1)
                    inner = get(x1, y1, x2, y2)

                    if outer == inner:
                        ans += 1

                k += 1

    # Diagonal (diamond) squares
    for i in range(n):
        for j in range(m):
            d = 1
            while True:
                x1, x2 = i - d, i + d
                y1, y2 = j - d, j + d

                if x1 < 0 or x2 >= n or y1 < 0 or y2 >= m:
                    break

                ok = True

                # check border
                for k in range(d+1):
                    if a[i-k][j-(d-k)] != '1': ok = False
                    if a[i-k][j+(d-k)] != '1': ok = False
                    if a[i+k][j-(d-k)] != '1': ok = False
                    if a[i+k][j+(d-k)] != '1': ok = False

                if not ok:
                    d += 1
                    continue

                # check no touching outside
                for x in range(x1-1, x2+2):
                    for y in range(y1-1, y2+2):
                        if 0 <= x < n and 0 <= y < m:
                            if abs(x - i) + abs(y - j) > d and a[x][y] == '1':
                                ok = False

                if ok:
                    ans += 1

                d += 1

    print(ans)