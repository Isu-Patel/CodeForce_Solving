d, sumTime = map(int, input().split())

mins = []
maxs = []

for _ in range(d):
   mn, mx = map(int, input().split())
   mins.append(mn)
   maxs.append(mx)

minSum = sum(mins)
maxSum = sum(maxs)

if sumTime < minSum or sumTime > maxSum:
   print("NO")
else:
   print("YES")

   schedule = mins[:]
   remaining = sumTime - minSum

   for i in range(d):
      can_add = min(maxs[i] - mins[i], remaining)
      schedule[i] += can_add
      remaining -= can_add

   print(*schedule)