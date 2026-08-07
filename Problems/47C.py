import sys

def solve():
    words = [input().strip() for _ in range(6)]
    
    best = None
    
    n = len(words)
    from itertools import permutations
    
    for perm in permutations(range(6)):
        w1 = words[perm[0]]
        w2 = words[perm[1]]
        w3 = words[perm[2]]
        w4 = words[perm[3]]
        w5 = words[perm[4]]
        w6 = words[perm[5]]

        r1 = len(w4) - 1
        total_h = len(w5)
        
        if len(w6) != total_h - r1:
            continue
        if r1 < 1 or (total_h - r1 - 1) < 1:
            continue
        
        c1 = len(w1) - 1
        total_w = len(w2)
        right_col = c1 + len(w6) - 1
        total_w = right_col + 1
        

        if len(w2) != total_w:
            continue

        c3_start = right_col - len(w3) + 1
        if c3_start < c1:
            continue
        if c3_start != c1:
            continue
        
        r2 = total_h - 1
        
        grid = [['.' for _ in range(total_w)] for _ in range(total_h)]
        
        ok = True
        def place_h(word, row, col_start):
            nonlocal ok
            for i, ch in enumerate(word):
                col = col_start + i
                if grid[row][col] != '.' and grid[row][col] != ch:
                    ok = False
                    return
                grid[row][col] = ch
        
        def place_v(word, col, row_start):
            nonlocal ok
            for i, ch in enumerate(word):
                row = row_start + i
                if grid[row][col] != '.' and grid[row][col] != ch:
                    ok = False
                    return
                grid[row][col] = ch
        
        place_h(w1, 0, 0)
        if not ok: continue
        place_h(w2, r1, 0)
        if not ok: continue
        place_h(w3, r2, c1)
        if not ok: continue
        place_v(w4, 0, 0)
        if not ok: continue
        place_v(w5, c1, 0)
        if not ok: continue
        place_v(w6, right_col, r1)
        if not ok: continue
        
        if not ok:
            continue
        
        result_lines = [''.join(row) for row in grid]
        candidate = tuple(result_lines)
        
        if best is None or candidate < best:
            best = candidate
    
    if best is None:
        print("Impossible")
    else:
        print('\n'.join(best))

solve()