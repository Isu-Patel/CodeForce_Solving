import sys

input = sys.stdin.readline

x1, y1, x2, y2, x3, y3 = map(int, input().split())

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def is_right(p1, p2, p3):
    d12 = dist_sq(p1, p2)
    d13 = dist_sq(p1, p3)
    d23 = dist_sq(p2, p3)
    if d12 + d13 == d23 or d12 + d23 == d13 or d13 + d23 == d12:
        return True
    return False

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)

if is_right(p1, p2, p3):
    print("RIGHT")
else:
    moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    almost = False
    for i, p in enumerate([p1, p2, p3]):
        for dx, dy in moves:
            np = (p[0] + dx, p[1] + dy)
            if i == 0:
                if is_right(np, p2, p3):
                    almost = True
                    break
            elif i == 1:
                if is_right(p1, np, p3):
                    almost = True
                    break
            else:
                if is_right(p1, p2, np):
                    almost = True
                    break
        if almost:
            break
    if almost:
        print("ALMOST")
    else:
        print("NEITHER")