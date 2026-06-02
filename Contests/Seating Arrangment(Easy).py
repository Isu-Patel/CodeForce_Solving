# Im doing on my own and posting on github to elp everyone practise

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, s = map(int, input().split())
    u = input().strip()

    dp = {(x, 0): 0}

    for ch in u:
        ndp = {}

        for (empty, avail), seated in dp.items():
            # Skip this person
            key = (empty, avail)
            if seated > ndp.get(key, -1):
                ndp[key] = seated

            if ch == 'I':
                if empty > 0:
                    ne = empty - 1
                    na = avail + (s - 1)
                    key = (ne, na)
                    if seated + 1 > ndp.get(key, -1):
                        ndp[key] = seated + 1

            elif ch == 'E':
                if avail > 0:
                    key = (empty, avail - 1)
                    if seated + 1 > ndp.get(key, -1):
                        ndp[key] = seated + 1

            else:  # 'A'
                if empty > 0:
                    ne = empty - 1
                    na = avail + (s - 1)
                    key = (ne, na)
                    if seated + 1 > ndp.get(key, -1):
                        ndp[key] = seated + 1

                if avail > 0:
                    key = (empty, avail - 1)
                    if seated + 1 > ndp.get(key, -1):
                        ndp[key] = seated + 1

        dp = ndp

    print(max(dp.values()))