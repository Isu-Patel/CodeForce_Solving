import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

houses = ['G', 'H', 'R', 'S']
names = {
    'G': 'Gryffindor',
    'H': 'Hufflepuff',
    'R': 'Ravenclaw',
    'S': 'Slytherin'
}

idx = {c: i for i, c in enumerate(houses)}

base = [0, 0, 0, 0]
variants = {(0, 0, 0, 0)}

for ch in s:
    if ch != '?':
        base[idx[ch]] += 1
        continue

    new_states = set()

    for state in variants:
        counts = [
            base[j] + state[j]
            for j in range(4)
        ]

        mn = min(counts)

        for j in range(4):
            if counts[j] == mn:
                nxt = list(state)
                nxt[j] += 1
                new_states.add(tuple(nxt))

    minimum = [
        min(state[j] for state in new_states)
        for j in range(4)
    ]

    for j in range(4):
        base[j] += minimum[j]

    variants = {
        tuple(state[j] - minimum[j] for j in range(4))
        for state in new_states
    }

possible = [False] * 4

for state in variants:
    counts = [
        base[j] + state[j]
        for j in range(4)
    ]

    mn = min(counts)

    for j in range(4):
        if counts[j] == mn:
            possible[j] = True

for ch in sorted(houses):
    if possible[idx[ch]]:
        print(names[ch])
