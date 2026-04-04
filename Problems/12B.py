n = input().strip()
m = input().strip()

digits = sorted(n)

if digits[0] == '0':
   for i in range(len(digits)):
      if digits[i] != '0':
         digits[0], digits[i] = digits[i], digits[0]
         break
smallest = ''.join(digits)

if smallest == m:
   print("OK")
else:
   print("WRONG_ANSWER")