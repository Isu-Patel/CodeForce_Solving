from collections import Counter

n, m = map(int, input().split())
nails = []
for _ in range(n):
    x, y = map(int, input().split())
    nails.append((x, y))
rods = list(map(int, input().split()))

def dist(i, j):
    dx = abs(nails[i][0] - nails[j][0])
    dy = abs(nails[i][1] - nails[j][1])
    return dx + dy

required = []
for i in range(n):
    prev_i = (i - 1) % n
    next_i = (i + 1) % n
    d = dist(prev_i, i) + dist(i, next_i)
    required.append(d)

def try_pattern(indices):
    needed_counter = Counter(required[i] for i in indices)
    rods_counter = Counter(rods)
    
    for length, count in needed_counter.items():
        if rods_counter[length] < count:
            return None
    
    rods_list = [(rods[i], i) for i in range(len(rods))]
    assignment = [-1] * n
    
    for i in indices:
        for j, (length, rod_idx) in enumerate(rods_list):
            if length == required[i]:
                assignment[i] = rod_idx + 1
                rods_list.pop(j)
                break
    
    return assignment

indices1 = list(range(0, n, 2))
indices2 = list(range(1, n, 2))

result = try_pattern(indices1)
if result is None:
    result = try_pattern(indices2)

if result is None:
    print("NO")
else:
    print("YES")
    print(' '.join(map(str, result)))