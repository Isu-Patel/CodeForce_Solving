import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

it = iter(data)
n = int(next(it))
m = int(next(it))
a = int(next(it))
b = int(next(it))
c = int(next(it))
if (n * m) % 2 == 1 or (n % 2 == 1 and m % 2 == 1):
    print("IMPOSSIBLE")
    sys.exit(0)

grid = [['?'] * m for _ in range(n)]
label_count = 0
def next_label():
    global label_count
    ch = chr(ord('a') + (label_count % 26))
    label_count += 1
    return ch