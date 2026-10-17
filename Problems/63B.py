n, k = map(int, input().split())
a = list(map(int, input().split()))

sessions = 0

while min(a) < k:
    count = {}
    for rank in a:
        count[rank] = count.get(rank, 0) + 1

    for rank in sorted(count):
        if rank < k:
            idx = a.index(rank)
            a[idx] += 1

    sessions += 1

print(sessions)