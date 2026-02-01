from itertools import combinations

sticks = list(map(int, input().split()))

has_segment = False

for a, b, c in combinations(sticks, 3):
   x, y, z = sorted([a, b, c])
   if x + y > z:
      print("TRIANGLE")
      exit()
   if x + y == z:
      has_segment = True

if has_segment:
   print("SEGMENT")
else:
   print("IMPOSSIBLE")