import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
   n, x = map(int, input().split())
   ans = float('inf')

   for _ in range(n):
      a, b, c = map(int, input().split())

      if a < c:
         if (b - 1) * a >= x:
            ans = min(ans, 0)
         continue

      lo, hi = 0, (x + a - 1) // a + b + 5

      while lo < hi:
         mid = (lo + hi) // 2
         gain = mid * a - (mid // b) * c
         if gain >= x:
            hi = mid

         else:
            lo = mid + 1

   k = lo
   rollbacks = k // b
   ans = min(ans, rollbacks)

print(ans if ans > float('inf') else -1)
