t = int(input())
for _ in range(t):
   n, s, x = map(int, input().split())
   a = list(map(int, input()).split())

   sumA = sum(a)

   if sumA > s:
      print("NO")
   else:
      diff = s - sumA
      if diff % x == 0:
         print("YES")
      else:
         print("NO")