n = int(input())

ans = []

left = 1
right = n

while left <= right:
    ans.append(left)
    left += 1

    if left <= right:
        ans.append(right)
        right -= 1

print(*ans)