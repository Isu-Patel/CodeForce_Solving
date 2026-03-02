import sys
input = sys.stdin.readline

n, v = map(int, input().split())

kayaks = []
cats = []

for i in range(1, n + 1):
    t, p = map(int, input().split())
    if t == 1:
        kayaks.append((p, i))
    else:
        cats.append((p, i))

# sort descending by capacity
kayaks.sort(reverse=True)
cats.sort(reverse=True)

# prefix sums
pref_k = [0]
for p, _ in kayaks:
    pref_k.append(pref_k[-1] + p)

pref_c = [0]
for p, _ in cats:
    pref_c.append(pref_c[-1] + p)

best_value = 0
best_k = 0
best_c = 0

max_c = min(len(cats), v // 2)

for c in range(max_c + 1):
    used_volume = 2 * c
    remaining = v - used_volume
    k = min(len(kayaks), remaining)
    
    total_value = pref_c[c] + pref_k[k]
    
    if total_value > best_value:
        best_value = total_value
        best_c = c
        best_k = k

print(best_value)

result = []

for i in range(best_c):
    result.append(str(cats[i][1]))

for i in range(best_k):
    result.append(str(kayaks[i][1]))

print(" ".join(result))