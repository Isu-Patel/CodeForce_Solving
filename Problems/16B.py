n, m = map(int, input().split())

containers = []

for _ in range(m):
    a, b = map(int, input().split())
    containers.append((b, a))  # store as (matches_per_box, boxes)

# sort by matches per box descending
containers.sort(reverse=True)

total_matches = 0

for b, a in containers:
    take = min(n, a)          # boxes we can take
    total_matches += take * b
    n -= take

    if n == 0:
        break

print(total_matches)