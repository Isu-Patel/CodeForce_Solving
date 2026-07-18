# This is the 4th Question Easy Version so i Will try my Best to Solve.
# Get the Code from Github if you want and there you can see all things.

import sys
import numpy as np

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    rng = np.random.default_rng(0xC0FFEE12345)
    out_lines = []
    for _ in range(t):
        n = int(data[idx]); q = int(data[idx+1]); idx += 2
        a = np.array(data[idx:idx+n], dtype=np.int64); idx += n
        idx += 2 * q
        if n == 1:
            out_lines.append('0'); continue
        s = np.sort(a)
        if np.array_equal(a, s):
            out_lines.append('0'); continue
        uniq, inv_a = np.unique(a, return_inverse=True)
        inv_s = np.searchsorted(uniq, s)
        randvals  = rng.integers(0, np.iinfo(np.uint64).max, size=len(uniq), dtype=np.uint64)
        randvals2 = rng.integers(0, np.iinfo(np.uint64).max, size=len(uniq), dtype=np.uint64)
        hashA, hashS   = randvals[inv_a],  randvals[inv_s]
        hash2A, hash2S = randvals2[inv_a], randvals2[inv_s]
        PA = np.empty(n+1, dtype=np.uint64); PA[0] = np.uint64(0)
        np.cumsum(hashA, out=PA[1:], dtype=np.uint64)
        PS = np.empty(n+1, dtype=np.uint64); PS[0] = np.uint64(0)
        np.cumsum(hashS, out=PS[1:], dtype=np.uint64)
        QA = np.empty(n+1, dtype=np.uint64); QA[0] = np.uint64(0)
        np.bitwise_xor.accumulate(hash2A, out=QA[1:])
        QS = np.empty(n+1, dtype=np.uint64); QS[0] = np.uint64(0)
        np.bitwise_xor.accumulate(hash2S, out=QS[1:])
        ans, L = None, 1
        while True:
            B = 1 << L
            lefts  = np.arange(0, n, B)
            rights = np.minimum(lefts + B, n)
            if (np.array_equal(PA[rights]-PA[lefts], PS[rights]-PS[lefts]) and
                np.array_equal(QA[rights]^QA[lefts], QS[rights]^QS[lefts])):
                ans = B >> 1
                break
            if B >= n:
                ans = B >> 1
                break
            L += 1
        out_lines.append(str(ans))
    sys.stdout.write('\n'.join(out_lines) + '\n')
main()