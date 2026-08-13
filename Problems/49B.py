a, b = input().split()

# Largest digit appearing in either number
max_digit = max(
    max(int(ch) for ch in a),
    max(int(ch) for ch in b)
)

# Minimum valid base
start = max_digit + 1

answer = 0

for base in range(start, 1002):
    # Convert the strings from base 'base' to decimal value
    x = 0
    for ch in a:
        x = x * base + int(ch)

    y = 0
    for ch in b:
        y = y * base + int(ch)

    total = x + y
    
    if total == 0:
        length = 1
    else:
        length = 0
        while total > 0:
            total //= base
            length += 1

    answer = max(answer, length)

print(answer)