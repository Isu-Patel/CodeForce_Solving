import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
   n = int(input())
   p = list(map(int, input().split()))

   suf = [0] * n
   suf[-1] = p[-1]
   for i in range(n - 2, -1, -1):
      suf[i] = max(p[i], suf[i + 1])

   l = -1
   for i in range(n):
      if p[i] < suf[i]:
         l = i
         break

   if l == -1:
      print(*p)
      continue

   target = suf[1]
   r = -1
   for i in range(n - 1, -1, -1):
      if p[i] == target:
         r = i
         break

         
   p[l:r + 1] = reversed(p[l:r + 1])

   print(*p)