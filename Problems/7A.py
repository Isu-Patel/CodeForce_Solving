board = [input().strip() for _ in range(8)]

row_count = 0
col_count = 0

for i in range(8):
   if board[i] == "BBBBBBBB":
      row_count += 1


if row_count == 8:
   print(8)
else:
   for j in range(8):
      all_black = True
      for i in range(8):
         if board[i][j] != "B":
            all_black = False
            break

      if all_black:
         col_count += 1
      
   print(row_count + col_count)

