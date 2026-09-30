n, m = map(int, input().split())

left = 1
right = n

for _ in range(m):
    hint = input().split()
    side = hint[2]
    i = int(hint[3])

    if side == "left":
        right = min(right, i - 1)
    else:  # "right"
        left = max(left, i + 1)

if left > right:
    print(-1)
else:
    print(right - left + 1)