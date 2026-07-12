#Hi this is the 4th question im trying to solve.

import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    
    LIMIT = 200010
    cost = [0] * (LIMIT + 5)
    for v in range(1, LIMIT + 5):
        bits = v.bit_length()
        pc = bin(v).count("1")
        cost[v] = bits + pc - 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = input_data[idx:idx+n]
        idx += n
        a = list(map(int, a))
        sumA = sum(a)
        
        ans = None
        for m in range(0, 21):
            C = 1 << m
            w = (40 // C) + 3
            total = 0
            for x in a:
                t0 = (x + C - 1) // C
                best = None
                for dt in range(w):
                    tt = t0 + dt
                    if tt > LIMIT:
                        break
                    val = C * tt + cost[tt]
                    if best is None or val < best:
                        best = val
                total += best
            candidate = total + m
            if ans is None or candidate < ans:
                ans = candidate
        
        out.append(str(ans - sumA))
    
    print("\n".join(out))

if __name__ == "__main__":
    main()