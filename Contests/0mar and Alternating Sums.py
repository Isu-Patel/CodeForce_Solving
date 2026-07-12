# Hi everyone here is the 3rd question for you all you guys can check.

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    MOD = 10**9 + 7
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n])); idx += n

        # group into blocks (array is guaranteed non-decreasing)
        blocks = []
        i = 0
        while i < n:
            j = i
            while j < n and a[j] == a[i]:
                j += 1
            blocks.append((a[i], j - i))
            i = j

        P = 1
        for val, c in blocks:
            P = P * pow(2, c - 1, MOD) % MOD

        vs = [val for val, c in blocks]

        E = {0: 1}
        O = {}
        ans_odd = 0

        for v in vs:
            d = E.get(-v, 0)
            ans_odd = (ans_odd + d) % MOD

            newE_add = {}
            for s, c in O.items():
                key = s - v
                newE_add[key] = newE_add.get(key, 0) + c

            newO_add = {}
            for s, c in E.items():
                key = s + v
                newO_add[key] = newO_add.get(key, 0) + c

            for k, c in newE_add.items():
                E[k] = (E.get(k, 0) + c) % MOD
            for k, c in newO_add.items():
                O[k] = (O.get(k, 0) + c) % MOD

        total = (1 + ans_odd) % MOD
        ans = (P * total) % MOD
        res.append(str(ans))

    sys.stdout.write("\n".join(res) + "\n")

solve()