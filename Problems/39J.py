import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

d = list(map(int, input().split()))
mosquitoes = list(map(int, input().split()))

counts = []

for jump in d:
    smashed = 0
    for pos in mosquitoes:
        if pos % jump == 0:
            smashed += 1
    counts.append(smashed)

mn = min(counts)

ans = [str(i + 1) for i in range(m) if counts[i] == mn]

print(len(ans))
print(" ".join(ans))