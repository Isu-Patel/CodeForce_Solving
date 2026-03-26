import sys

# Read all lines
lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# Find maximum length
max_len = max(len(line) for line in lines)

# Width of the frame content (excluding the asterisks)
width = max_len

# Print top border
print('*' * (width + 2))

# Track which side gets extra space for uneven padding
left_turn = True

# Print each line centered
for line in lines:
    line_len = len(line)
    total_padding = width - line_len
    
    if total_padding == 0:
        # No padding needed
        print('*' + line + '*')
    else:
        # Calculate left and right padding
        left_pad = total_padding // 2
        right_pad = total_padding - left_pad
        
        # If padding is odd, alternate which side gets extra space
        if total_padding % 2 == 1:
            if left_turn:
                # Extra space goes to the right (less on left)
                pass  # left_pad and right_pad already set correctly
            else:
                # Extra space goes to the left (less on right)
                left_pad += 1
                right_pad -= 1
            left_turn = not left_turn
        
        print('*' + ' ' * left_pad + line + ' ' * right_pad + '*')

# Print bottom border
print('*' * (width + 2))
