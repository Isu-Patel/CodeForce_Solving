from itertools import permutations

s = []
for _ in range(3):
    x = input().strip()
    x = ''.join(c.lower() for c in x if c not in '-;_')
    s.append(x)

possible = set()

for p in permutations(s):
    possible.add(''.join(p))

n = int(input())

for _ in range(n):
    ans = input().strip()

    ans = ''.join(c.lower() for c in ans if c not in '-;_')

    if ans in possible:
        print("ACC")
    else:
        print("WA")