import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

if len(s) != len(t):
    print(-1)
    sys.exit()

n = int(input())

INF = 10**18

dist = [[INF] * 26 for _ in range(26)]

for i in range(26):
    dist[i][i] = 0

for _ in range(n):
    a, b, w = input().split()
    w = int(w)

    u = ord(a) - ord('a')
    v = ord(b) - ord('a')

    dist[u][v] = min(dist[u][v], w)

for k in range(26):
    for i in range(26):
        dik = dist[i][k]
        if dik == INF:
            continue
        for j in range(26):
            nd = dik + dist[k][j]
            if nd < dist[i][j]:
                dist[i][j] = nd

answer_cost = 0
result = []

for a, b in zip(s, t):
    x = ord(a) - ord('a')
    y = ord(b) - ord('a')

    best_cost = INF
    best_char = -1

    for c in range(26):
        if dist[x][c] == INF or dist[y][c] == INF:
            continue

        cur = dist[x][c] + dist[y][c]

        if cur < best_cost:
            best_cost = cur
            best_char = c

    if best_char == -1:
        print(-1)
        sys.exit()

    answer_cost += best_cost
    result.append(chr(best_char + ord('a')))

print(answer_cost)
print("".join(result))