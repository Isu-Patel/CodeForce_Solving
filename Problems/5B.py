import sys

lines = sys.stdin.read().splitlines()

width = max(len(line) for line in lines)

border = "*" * (width + 2)
print(border)

left_turn = True

for line in lines:
   spaces = width - len(line)

   left = spaces // 2
   right = spaces - left

   if spaces % 2 == 1:
      if left_turn:
         right -= 1
         left += 1
      left_turn = not left_turn

   print("*" + " " * left + line + " " * right + "*")

print(border)