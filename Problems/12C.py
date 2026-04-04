n, m = map(int, input().split())
prices = list(map(int, input().split()))

from collections import Counter

fruits = [input().strip() for _ in range(m)]
freq = list(Counter(fruits).values())

# Sort
prices.sort()
freq.sort(reverse=True)

# Minimum cost
min_cost = 0
for i in range(len(freq)):
    min_cost += freq[i] * prices[i]

# Maximum cost
max_cost = 0
for i in range(len(freq)):
    max_cost += freq[i] * prices[n - 1 - i]

print(min_cost, max_cost)