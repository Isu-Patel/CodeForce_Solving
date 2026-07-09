n, b = map(int, input().split())
a = list(map(int, input().split()))

min_price = a[0]
answer = b

for price in a:
    dollars = b // min_price
    money = b % min_price + dollars * price
    answer = max(answer, money)
    min_price = min(min_price, price)

print(answer)