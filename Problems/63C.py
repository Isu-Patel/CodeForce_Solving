from itertools import permutations

n = int(input())
guesses = []

for _ in range(n):
    a, b, c = input().split()
    guesses.append((a, int(b), int(c)))

possible = []

for digits in permutations("0123456789", 4):
    candidate = ''.join(digits)
    valid = True

    for guess, bulls, cows in guesses:
        actual_bulls = sum(
            candidate[i] == guess[i] for i in range(4)
        )

        actual_cows = sum(
            d in guess for d in candidate
        ) - actual_bulls

        if actual_bulls != bulls or actual_cows != cows:
            valid = False
            break

    if valid:
        possible.append(candidate)

if len(possible) == 0:
    print("Incorrect data")
if len(possible) == 1:
    print(possible[0])
else:
    print("Need more data")
    