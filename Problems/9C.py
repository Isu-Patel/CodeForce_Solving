from collections import deque

n = int(input())

q = deque(["1"])
count = 0

while q:
   s = q.popleft()
   num = int(s)

   if num > n:
      continue
   
   count += 1

   q.append(s + "0")
   q.append(s + "1")

print(count)