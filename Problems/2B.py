import sys

input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def count_factors(x, f):
    cnt = 0
    while x > 0 and x % f == 0:
      x //= f
      cnt += 1
    return cnt

c2 = [[0] * n for _ in range(n)]
c5 = [[0] * n for _ in range(n)]

zero_pos = None

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            zero_pos = (i, j)
            c2[i][j] = c5[i][j] == 10 ** 9
        else:
            c2[i][j] = count_factors(a[i][j], 2)
            c5[i][j] = count_factors(a[i][j], 5)

INF = 10 ** 18
dp2 = [[INF] * n for _ in range(n)]
dp5 = [[INF] * n for _ in range(n)]

p2 = [[None] * n for _ in range(n)]
p5 = [[None] * n for _ in range(n)]

dp2[0][0] = c2[0][0]
dp5[0][0] = c5[0][0]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            continue

        if i > 0 and dp2[i - 1][j] + c2[i][j] < dp2[i][j]:
            dp2[i][j] = dp2[i - 1][j] + c2[i][j]
            p2[i][j] = 'D'
        if j > 0 and dp2[i][j - 1] + c2[i][j] < dp2[i][j]:
            dp2[i][j] = dp2[i][j - 1] + c2[i][j]
            p2[i][j] = 'R'

        if i > 0 and dp5[i - 1][j] + c5[i][j] < dp5[i][j]:
            dp5[i][j] = dp5[i - 1][j] + c5[i][j]
            p5[i][j] = 'D'
        
        if j > 0 and dp5[i][j - 1] + c5[i][j] < dp5[i][j]:
            dp5[i][j] = dp5[i][j - 1] + c5[i][j]
            p5[i][j] = 'R'

end2 = dp2[n - 1][n - 1]
end5 = dp5[n - 1][n - 1]
best = min(end2, end5)

if zero_pos and best > 1:
    print(1)
    zi, zj = zero_pos
    path = []
    path += ['D'] * zi
    path += ['R'] * zj
    path += ['D'] * (n - 1 - zi)
    path += ['R'] * (n - 1 - zj)
    print("".join(path))
    sys.exit()

print(best)

if end2 < end5:
    parent = p2
else:
    parent = p5

i, j = n - 1, n - 1

path = []

while i > 0 or j > 0:
    move = parent[i][j]
    path.append(move)
    if move == 'D':
        i -= 1
    else:
        j -= 1

path.reverse()
print("".join(path))