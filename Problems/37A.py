from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)

largest_tower = max(cnt.values())
total_towers = len(cnt)

print(largest_tower, total_towers)