import sys

input = sys.stdin.readline

N, K = map(int, input().split())
P = input().strip()
mask = input().strip()

m = len(P)

s = [-1] * N

for i in range(N - m + 1):
    if mask[i] == '1':
        for j in range(m):
            pos = i + j

            if s[pos] != -1 and s[pos] != P[j]:
                print("No solution")
                sys.exit()

            s[pos] = P[j]

fill = 'a' if P[0] != 'a' else 'b'

for i in range(N):
    if s[i] == -1:
        s[i] = fill

s = ''.join(s)

for i in range(N - m + 1):
    occurs = (s[i:i + m] == P)

    if mask[i] == '1':

        if not occurs:
            print("No solution")
            sys.exit()
    else:
        if occurs:
            print("No solution")
            sys.exit()

print(s)