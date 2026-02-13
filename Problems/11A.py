n, d = map(int, input().split())
b = list(map(int, input().split()))

moves = 0

for i in range(1, n):
   if b[i] <= b[i - 1]:
      diff = b[i - 1] - b[i]
      k = diff // d + 1
      b[i] += k * d
      moves += k

print(moves)
