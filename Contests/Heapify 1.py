import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
   n = int(input())
   a = list(map(int, input().split()))

   visited = [False] * (n + 1)
   possible = True

   for i in range(1, n + 1):
      if visited[i]:
         continue

      stack = [i]
      comp = []

      while stack:
         x = stack.pop()
         if visited[x]:
            continue
         visited[x] = True
         comp.append(x)

         if 2 * x <= n and not visited[2 * x]:
            stack.append(2 * x)
         if x % 2 == 0 and not visited[x // 2]:
            stack.append(x // 2)

      current = [a[idx - 1] for idx in comp]

      target = comp[:]

      if sorted(current) != sorted(target):
         possible = False
         break

   print("YES" if possible else "NO")