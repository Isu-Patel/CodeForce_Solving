n, m = map(int, input().split())

prev_color = None

for i in range(n):
    row = input().strip()
    
    # check if row has same color
    if len(set(row)) != 1:
        print("NO")
        exit()
    
    color = row[0]
    
    # check adjacent row color
    if color == prev_color:
        print("NO")
        exit()
    
    prev_color = color

print("YES")