n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

a, b = map(int, input().split())

pref = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        pref[i + 1][j + 1] = (
            grid[i][j]
            + pref[i][j + 1]
            + pref[i + 1][j]
            - pref[i][j]
        )


def rectangle_sum(r1, c1, r2, c2):
    return (
        pref[r2][c2]
        - pref[r1][c2]
        - pref[r2][c1]
        + pref[r1][c1]
    )


INF = 10**9
answer = INF

if a <= n and b <= m:
    for i in range(n - a + 1):
        for j in range(m - b + 1):
            answer = min(
                answer,
                rectangle_sum(i, j, i + a, j + b)
            )

if b <= n and a <= m:
    for i in range(n - b + 1):
        for j in range(m - a + 1):
            answer = min(
                answer,
                rectangle_sum(i, j, i + b, j + a)
            )

print(answer)
