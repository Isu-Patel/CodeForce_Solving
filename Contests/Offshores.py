t = int(input())

for _ in range(t):
   n, x, y = map(int, input().split())
   a = list(map(int, input().split()))

   total_transfers = 0
   best_value = 0

   for money in a:
      transfers = money // x
      total_transfers += transfers
      best_value = max(best_value, money - transfers * y)

   answer = total_transfers * y + best_value
   print(answer)