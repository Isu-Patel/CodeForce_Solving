import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M_list = list(map(int, input().split()))

used = [[0] * (K + 1) for _ in range(K + 1)]

cx = (K + 1) // 2
cy = (K + 1) // 2

for m in M_list:
    best_cost = float('inf')
    best_x = -1
    best_l = -1
    best_r = -1

    for x in range(1, K + 1):
        for yl in range(1, K - m + 2):
            yr = yl + m - 1

            # Check if segment is free
            ok = True
            for y in range(yl, yr + 1):
                if used[x][y]:
                    ok = False
                    break
            if not ok:
                continue

            # Compute cost
            cost = 0
            for y in range(yl, yr + 1):
                cost += abs(x - cx) + abs(y - cy)

            # Choose best
            if (cost < best_cost or
                (cost == best_cost and (x < best_x or
                (x == best_x and yl < best_l)))):

                best_cost = cost
                best_x = x
                best_l = yl
                best_r = yr

    if best_x == -1:
        print(-1)
    else:
        print(best_x, best_l, best_r)
        for y in range(best_l, best_r + 1):
            used[best_x][y] = 1