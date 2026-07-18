# This is the 4th Question(Hard) Version of 4th Topic.
# You can check it out on GitHub.

import sys
import random

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    R1 = random.Random(12345)
    R2 = random.Random(67890)
    MASK = (1 << 64) - 1

    for _ in range(t):
        n = int(data[idx]); q = int(data[idx+1]); idx += 2
        a = data[idx:idx+n]; idx += n
        a = [int(x) for x in a]
        upd_i = [0]*q
        upd_x = [0]*q
        for k in range(q):
            i = int(data[idx]); x = int(data[idx+1]); idx += 2
            upd_i[k] = i
            upd_x[k] = x

        vals = sorted(set(a) | set(upd_x))
        vmap = {v: i for i, v in enumerate(vals)}
        m = len(vals)
        h1 = [R1.getrandbits(64) for _ in range(m)]
        h2 = [R2.getrandbits(64) for _ in range(m)]

        maxL = 0
        while (1 << maxL) < n:
            maxL += 1

        cur = [vmap[x] for x in a]

        cnt = [0]*m
        for c in cur:
            cnt[c] += 1
        sorted_vals_order = []
        for vi in range(m):
            if cnt[vi]:
                sorted_vals_order.extend([vi]*cnt[vi])

        srt = sorted_vals_order

        p0 = [0]*(n+1)
        x0 = [0]*(n+1)
        acc = 0
        accx = 0
        for i in range(n):
            acc = (acc + h1[cur[i]]) & MASK
            p0[i+1] = acc
            accx ^= h2[cur[i]]
            x0[i+1] = accx

        spre = [0]*(n+1)
        sxr = [0]*(n+1)
        acc = 0
        accx = 0
        for i in range(n):
            acc = (acc + h1[srt[i]]) & MASK
            spre[i+1] = acc
            accx ^= h2[srt[i]]
            sxr[i+1] = accx

        def compute_f():
            if p0[n] == spre[n] and x0[n] == sxr[n]:
                if cur == srt:
                    return 0
            L = 1
            while True:
                B = 1 << L
                ok = True
                for l in range(0, n, B):
                    r = l+B
                    if r > n: r = n
                    if (p0[r]-p0[l]) & MASK != (spre[r]-spre[l]) & MASK:
                        ok = False
                        break
                    if (x0[r]^x0[l]) != (sxr[r]^sxr[l]):
                        ok = False
                        break
                if ok:
                    return B >> 1
                if B >= n:
                    return B >> 1
                L += 1

        out.append(str(compute_f()))

        for k in range(q):
            i = upd_i[k]; xv = vmap[upd_x[k]]
            old = cur[i]
            if old != xv:
                cnt[old] -= 1
                cnt[xv] += 1
                oh1 = h1[old]; oh2 = h2[old]
                nh1 = h1[xv]; nh2 = h2[xv]
                for j in range(i+1, n+1):
                    p0[j] = (p0[j] - oh1 + nh1) & MASK
                    x0[j] ^= oh2 ^ nh2
                cur[i] = xv

                pos = 0
                acc = 0
                accx = 0
                for vi in range(m):
                    c = cnt[vi]
                    if c:
                        hh1 = h1[vi]; hh2 = h2[vi]
                        for _ in range(c):
                            acc = (acc + hh1) & MASK
                            pos += 1
                            spre[pos] = acc
                            accx ^= hh2
                            sxr[pos] = accx
                srt = None

            out.append(str(compute_f()))

    sys.stdout.write('\n'.join(out) + '\n')

main()