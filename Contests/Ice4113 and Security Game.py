# Hello Everyone this is the question E. I will try to solve if i can.

import sys

def main():
    data = sys.stdin
    t = int(data.readline())
    FULL = (1 << 30) - 1
    for _ in range(t):
        print(FULL)
        sys.stdout.flush()
        o = int(data.readline())
        m0 = 0
        m1 = o
        print(m0, m1)
        sys.stdout.flush()
        r = int(data.readline())
        b = 0 if r == o else 1
        print(b)
        sys.stdout.flush()

if __name__ == "__main__":
    main()