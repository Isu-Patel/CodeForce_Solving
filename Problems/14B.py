n, x0 = map(int, input().split())

left_max = 0
right_min = 1000

for _ in range(n):
    a, b = map(int, input().split())
    
    # Normalize segment
    if a > b:
        a, b = b, a
    
    # Update intersection bounds
    left_max = max(left_max, a)
    right_min = min(right_min, b)

# Check if intersection exists
if left_max > right_min:
    print(-1)
elif left_max <= x0 <= right_min:
    # Bob is already in the intersection
    print(0)
else:
    # Find minimum distance to the intersection
    if x0 < left_max:
        print(left_max - x0)
    else:  # x0 > right_min
        print(x0 - right_min)
