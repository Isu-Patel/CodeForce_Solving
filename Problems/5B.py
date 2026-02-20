import sys

# read all lines (including empty ones)
lines = sys.stdin.read().splitlines()

# find max width
width = max(len(line) for line in lines)

border = "*" * (width + 2)
print(border)

left_turn = True  # for alternating extra space

for line in lines:
    L = len(line)
    total = width - L
    
    left = total // 2
    right = total // 2
    
    if total % 2 == 1:
        if left_turn:
            left += 1
        else:
            right += 1
        left_turn = not left_turn
    
    print("*" + " " * left + line + " " * right + "*")

print(border)