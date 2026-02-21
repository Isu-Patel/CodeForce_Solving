t = int(input())

for _ in range(t):
   n = int(input())
   s = input().strip()

   ans = 1

   for shift in range(n):
      # rotate
      r = s[shift:] + s[:shift]

      # count blocks
      blocks = 1
      for i in range(1, n):
         if r[i] != r[i - 1]:
            blocks += 1

      ans = max(ans, blocks)

   print(ans)