import math
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, C = map(int, data[:3])

    if A == 0:
        if B == 0:
            if C == 0:
                print(-1)
            else:
                print(0)
        else:
            x = -C / B
            print(1)
            print(f"{x:.10f}")
        return

    D = B * B - 4 * A * C
    if D < 0:
        print(0)
    elif D == 0:
        x = -B / (2 * A)
        print(1)
        print(f"{x:.10f}")
    else:
        sqrtD = math.sqrt(D)
        x1 = (-B - sqrtD) / (2 * A)
        x2 = (-B + sqrtD) / (2 * A)
        roots = sorted([x1, x2])
        print(2)
        print(f"{roots[0]:.10f}")
        print(f"{roots[1]:.10f}")

if __name__ == '__main__':
    main()
