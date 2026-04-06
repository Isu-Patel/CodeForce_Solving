segments = [list(map(int, input().split())) for _ in range(4)]

h = []  # horizontal
v = []  # vertical

for x1, y1, x2, y2 in segments:
    if y1 == y2:
        h.append((min(x1,x2), max(x1,x2), y1))
    elif x1 == x2:
        v.append((x1, min(y1,y2), max(y1,y2)))
    else:
        print("NO")
        exit()

# must be exactly 2 each
if len(h) != 2 or len(v) != 2:
    print("NO")
    exit()

# sort for consistency
h.sort()
v.sort()

# unpack
(x1, x2, yA) = h[0]
(x3, x4, yB) = h[1]

(xL, y1, y2) = v[0]
(xR, y3, y4) = v[1]

# horizontal lengths must match
if x1 != x3 or x2 != x4:
    print("NO")
    exit()

# vertical lengths must match
if y1 != y3 or y2 != y4:
    print("NO")
    exit()

# must connect properly
if yA != y1 or yB != y2:
    print("NO")
    exit()

if xL != x1 or xR != x2:
    print("NO")
    exit()

# positive area
if x1 == x2 or y1 == y2:
    print("NO")
else:
    print("YES")