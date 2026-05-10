import sys

data = sys.stdin.read().split()
A1 = int(data[0])
B1 = int(data[1])
C1 = int(data[2])
A2 = int(data[3])
B2 = int(data[4])
C2 = int(data[5])

det = A1 * B2 - A2 * B1
if det != 0:
    print(1)
else:
    if A1 * C2 - A2 * C1 == 0:
        print(-1)
    else:
        print(0)
        
