n = int(input())
s = input().strip()

h = s.count('H')

if h == 0 or h == n:
    print(0)
    exit()

t = s + s


inside = t[:h].count('H')
best = inside

for i in range(1, n):
    if t[i - 1] == 'H':
        inside -= 1

    if t[i + h - 1] == 'H':
        inside += 1

    best = max(best, inside)

print(h - best)
