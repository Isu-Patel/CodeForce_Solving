t = int(input())

for _ in range(t):
   n, h, l = map(int, input().split())
   a = list(map(int, input().split()))

   row_only = 0
   col_only = 0
   both = 0

   for x in a:
      if x <= h and x <= 1:
         both += 1
      elif x <= h:
         row_only += 1
      elif x <= 1:
         col_only += 1  

   p1 = min(row_only, col_only)
   row_only -= p1
   col_only -= p1
   
   p2 = min(row_only, both)
   both -= p2

   p3 = min(col_only, both)
   both -= p3

   p4 = both // 2

   print(p1 + p2 + p3 + p4)
   # cnt_row = sum(1 for x in a if x <= h)
   # cnt_col = sum(1 for x in a if x <= 1)

   # ans = min(n // 2, cnt_row, cnt_col)
   # print(ans)