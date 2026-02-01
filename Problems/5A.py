import sys

users = set()
total = 0

for raw in sys.stdin:
   line = raw.rstrip('\n')

   if not line:
      continue

   first = line[0]

   if first == '+':
      users.add(line[1:])

   elif first == '-':
      users.remove(line[1:])

   else:

      idx = line.find(':')
      sender = line[:idx]
      msg = line[idx + 1:]

      total += len(msg) * len(users)

   
print(total)

