import sys

input = sys.stdin.readline

n = int(input())
lengths = list(map(int, input().split()))

order = sorted([(lengths[i], i) for i in range(n)])

ans = [""] * n

cur = 0
prev_len = 0

for length, idx in order:
    cur <<= (length - prev_len)

    if cur >= (1 << length):
        print("NO")
        sys.exit()

    ans[idx] = format(cur, '0{}b'.format(length))

    cur += 1
    prev_len = length

print("YES")
print(*ans, sep="\n")