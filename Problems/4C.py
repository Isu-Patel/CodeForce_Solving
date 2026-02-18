n = int(input())

db = {}

for _ in range(n):
   name = input().strip()

   if name not in db:
      print("OK")
      db[name] = 1
   else:
      new_name = name + str(db[name])
      print(new_name)

      db[name] += 1

      db[new_name] = 1
      