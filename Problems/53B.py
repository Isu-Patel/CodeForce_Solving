import sys

h, w = map(int, input().split())

best_h = 0
best_w = 0
best_area = -1

p = 1

while p <= max(h, w):
    # p is the height
    if p <= h:
        # 4*p/5 <= width <= 5*p/4
        low = (4 * p + 4) // 5
        high = (5 * p) // 4

        width = min(w, high)

        if width >= low:
            area = p * width

            if area > best_area or (area == best_area and p > best_h):
                best_area = area
                best_h = p
                best_w = width

    # p is the width
    if p <= w:
        # 4*height/5 <= p <= 5*height/4
        low = (4 * p + 4) // 5
        high = (5 * p) // 4

        height = min(h, high)

        if height >= low:
            area = height * p

            if area > best_area or (area == best_area and height > best_h):
                best_area = area
                best_h = height
                best_w = p

    p *= 2

print(best_h, best_w)