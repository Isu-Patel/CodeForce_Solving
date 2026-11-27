import re
import sys


data = sys.stdin.read()
match = re.match(r"\s*(\d+)", data)
n = int(match.group(1))
relations = re.sub(r"\s+", "", data[match.end():])

group_sizes = [1]
group_relations = []

for relation in relations:
    if relation == "=":
        group_sizes[-1] += 1
    else:
        group_relations.append(relation)
        group_sizes.append(1)

groups = [1] * len(group_sizes)
for i, relation in enumerate(group_relations):
    if relation == "R":
        groups[i + 1] = groups[i] + 1

for i in range(len(group_relations) - 1, -1, -1):
    if group_relations[i] == "L":
        groups[i] = max(groups[i], groups[i + 1] + 1)

expanded = []
for size, candies in zip(group_sizes, groups):
    expanded.extend([candies] * size)

print(*expanded)