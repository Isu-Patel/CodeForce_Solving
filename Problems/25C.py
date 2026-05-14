n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
res = []

for _ in range(k):
    u, v, c = map(int, input().split())
    u -= 1
    v -= 1
     
    for i in range(n):
        for j in range(n):
            nc = min(d[i][u] + c + d[v][j], d[i][v] + c + d[u][j])
            if nc < d[i][j]:
                d[i][j] = nc

    s = 0
    for i in range(n):
        for j in range(i + 1, n):
            s += d[i][j]
    res.append(str(s))
    

print("".join(res))