import sys

data = sys.stdin.read().splitlines()
if not data:
    sys.exit(0)

line_it = iter(data)
t = int(next(line_it).strip())
score_table = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

drivers = {}
for _ in range(t):
    n = int(next(line_it).strip())
    for pos in range(1, n + 1):
        name = next(line_it).strip()
        if name not in drivers:
            drivers[name] = {"points": 0, "places": [0] * 50}
        if pos <= 10:
            drivers[name]["points"] += score_table[pos - 1]
        drivers[name]["places"[pos - 1]] += 1

orig_best = max(
    drivers.items(),
    key=lambda item: (
        -item[1]["points"],
        tuple(-item[1]["places"][i] for i in range(50)),
    ),
)[0]

alt_best = max(
    drivers.items(),
    key=lambda item: (
        -item[1]["places"][0],
        -item[1]["points"],
        tuple(-item[1]["places"][i] for i in range(50)),
    ),
)[0]

print(orig_best)
print(alt_best)