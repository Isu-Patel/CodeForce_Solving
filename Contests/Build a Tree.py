# Hi this is the 5 th Question I tried to solve it.
# And you can all check it out at Github

import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    res = []
    for _ in range(t):
        n = int(input_data[idx]); k = int(input_data[idx+1]); idx += 2
        min_k = 2*n - 2 if n > 2 else 2
        if n == 2:
            min_k = 2
        
        max_k = (n * n) // 2
        
        if k < min_k or k > max_k:
            res.append("-1")
            continue
        
        order = []
        lo, hi = 1, n
        toggle = True
        while lo <= hi:
            if toggle:
                order.append(lo)
                lo += 1
            else:
                order.append(hi)
                hi -= 1
            toggle = not toggle
        
        pos = [0] * (n + 1)
        for i, v in enumerate(order):
            pos[v] = i
        
        def compute_sum(pos_arr):
            s = 0
            for i in range(1, n + 1):
                j = (i % n) + 1
                s += abs(pos_arr[i] - pos_arr[j])
            return s
        
        cur_k = compute_sum(pos)
        
        pos_arr = pos[:]
        order_arr = order[:]
        
        cur = cur_k
        
        def delta_swap(p):
            nonlocal cur
            a_lbl = order_arr[p]
            b_lbl = order_arr[p+1]
        
            affected_labels = set()
            for lbl in (a_lbl, b_lbl):
                affected_labels.add(lbl)
                nxt = (lbl % n) + 1
                prv = ((lbl - 2) % n) + 1
                affected_labels.add(nxt)
                affected_labels.add(prv)
        
            old_contrib = 0
            edges_to_check = set()
            for lbl in affected_labels:
                nxt = (lbl % n) + 1
                edges_to_check.add((lbl, nxt))
            for (u, v) in edges_to_check:
                old_contrib += abs(pos_arr[u] - pos_arr[v])
        
            pos_arr[a_lbl], pos_arr[b_lbl] = pos_arr[b_lbl], pos_arr[a_lbl]
            order_arr[p], order_arr[p+1] = b_lbl, a_lbl
            new_contrib = 0
            for (u, v) in edges_to_check:
                new_contrib += abs(pos_arr[u] - pos_arr[v])
            cur += (new_contrib - old_contrib)
        
        
        max_passes = 4 * n
        passes = 0
        while cur > k and passes < max_passes:
            progressed = False
            for p in range(n - 1):
                if cur <= k:
                    break
                before = cur
                delta_swap(p)
                if cur < k:
                    
                    delta_swap(p)
                elif cur < before:
                    progressed = True
            passes += 1
            if not progressed:
                break
        
        if cur != k:
            res.append("-1")
            continue
        
        edges = []
        for i in range(n - 1):
            edges.append((order_arr[i], order_arr[i+1]))
        
        res.append('\n'.join(f"{u} {v}" for u, v in edges))
    
    sys.stdout.write('\n'.join(res) + '\n')

solve()