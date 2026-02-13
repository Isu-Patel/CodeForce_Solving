t = int(input())

for _ in range(t):
   n, w = map(int, input().split())

   if w == 1:
      print(0)
   else:
      kept = n // w
      print(n - kept)