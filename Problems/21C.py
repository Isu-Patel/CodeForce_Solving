import sys

data = sys.stdin.read().split()
n = int(data[0])
a = list(map(int, data[1:]))

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

total = s[n]
if total % 3 != 0:
    print(0)
else:
    target = total // 3
    count = 0
    num_left = 0
    for k in range(1, n + 1):
        if s[k] == 2 * target and k < n:
            count += num_left
        if s[k - 1] == target:
            num_left += 1

    print(count)