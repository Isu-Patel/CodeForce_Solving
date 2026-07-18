# Hi this is the 3rd Question
# I tried my best you can check it at Github.

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = data[idx:idx+n]; idx += n
        b = data[idx:idx+n]; idx += n
        p = 0   # a=1,b=0
        q = 0   # a=0,b=1
        M = 0   # a=1,b=1 (matching ones)
        Z = 0   # a=0,b=0 (matching zeros)
        for i in range(n):
            ai = a[i]; bi = b[i]
            if ai == b'1':
                if bi == b'0': p += 1
                else: M += 1
            else:
                if bi == b'1': q += 1
                else: Z += 1
        if p == 0 and q == 0:
            out.append('0')
        elif p % 2 == 1:
            out.append('1')
        elif p > 0:
            out.append('2')
        else:
            out.append('2' if (M >= 1 and Z >= 1) else '-1')
    sys.stdout.write('\n'.join(out) + '\n')

main()