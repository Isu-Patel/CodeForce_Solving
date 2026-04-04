import sys
input = sys.stdin.readline

N = int(input())

cnt = [0] * 10

for i in range(1, N + 1):
    r = i % 9
    if r == 0:
        r = 9
    cnt[r] += 1

# Function to compute digital root
def dr(x):
    x %= 9
    return 9 if x == 0 else x

total = 0

for da in range(1, 10):
    for db in range(1, 10):
        dc = dr(da * db)
        total += cnt[da] * cnt[db] * cnt[dc]


correct = 0

for a in range(1, N + 1):
    for b in range(1, N // a + 1):
        correct += 1  # because c = a*b ≤ N

print(total - correct)