from collections import Counter

n = int(input())

names = [input().strip() for _ in range(n)]
surnames = [input().strip() for _ in range(n)]

names.sort()
surnames.sort()

name_count = Counter(name[0] for name in names)
surname_count = Counter(s[0] for s in surnames)

max_matches = sum(
    min(name_count[ch], surname_count[ch])
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

remaining_surnames = surnames[:]
remaining_names = Counter(name[0] for name in names)

matches_done = 0
answer = []

for name in names:
    first = name[0]

    remaining_names[first] -= 1

    for j, surname in enumerate(remaining_surnames):
        sf = surname[0]

        surname_count[sf] -= 1

        current_match = 1 if first == sf else 0

        possible_future = 0

        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            possible_future += min(
                remaining_names[ch],
                surname_count[ch]
            )

        if matches_done + current_match + possible_future == max_matches:
            answer.append(name + " " + surname)

            matches_done += current_match
            remaining_surnames.pop(j)
            break

        surname_count[sf] += 1

print(", ".join(answer))