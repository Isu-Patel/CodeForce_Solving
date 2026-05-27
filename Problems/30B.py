from itertools import permutations

# Read finals date
FD, FM, FY = input().split('.')
FD, FM, FY = int(FD), int(FM), int(FY)

# Read Bob's passport date
parts = input().split('.')
nums = [int(x) for x in parts]

# Days in months
def leap(y):
    return y % 4 == 0

def valid(d, m, y):
    if not (1 <= m <= 12):
        return False

    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if leap(y):
        days[1] = 29#0

    return 1 <= d <= days[m - 1]

# Compare dates
# returns True if birth <= finals-18years
def old_enough(bd, bm, by):
    target_y = FY - 18

    # same century required
    if by <= 0:
        return False

    if by < target_y:
        return True

    if by > target_y:
        return False

    # same year
    if bm < FM:
        return True

    if bm > FM:
        return False

    return bd <= FD


ok = False

for d, m, y in permutations(nums):
    
    if not valid(d, m, y):
        continue

    if old_enough(d, m, y):
        ok = True
        break

print("YES" if ok else "NO")