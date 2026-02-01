t = int(input())

for _ in range(t):
   n = int(input())

   p = [0] * (n + 1)
   used = [False] * (n + 1)

   p[n - 1] = 1
   p[n] = n
   used[1] = used[n] = True

   for i in range(n - 2, 0, -1):
      y = p[i + 1]

      x1 = y + i
      x2 = y - i

      if 1 <= x1 <= n and not used[x1]:
         p[i] = x1
         used[x1] = True
      else:
         p[i] = x2
         used[x2] = True

print(*p[1:])