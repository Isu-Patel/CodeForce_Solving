import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())

# Formula 1 points
score = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# stats[name] = [points, places[]]
stats = defaultdict(lambda: [0, [0]*50])

for _ in range(t):
    n = int(input())

    for pos in range(n):
        name = input().strip()

        # points
        if pos < 10:
            stats[name][0] += score[pos]

        # count finishing positions
        stats[name][1][pos] += 1


drivers = list(stats.keys())

# ---------- Original System ----------
# points -> wins -> 2nd -> 3rd ...
champ1 = max(
    drivers,
    key=lambda x: (
        stats[x][0],          # points
        *stats[x][1]          # places
    )
)

# ---------- Alternative System ----------
# wins -> points -> 2nd -> 3rd ...
champ2 = max(
    drivers,
    key=lambda x: (
        stats[x][1][0],       # wins
        stats[x][0],          # points
        *stats[x][1][1:]      # remaining places
    )
)

print(champ1)
print(champ2)