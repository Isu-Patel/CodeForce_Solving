grid = [input().strip() for _ in range(3)]

for i in range(3):
   for j in range(3):
      if grid[i][j] != grid[2 - i][2 - j]:
         print("NO")
         exit()

print("YES")