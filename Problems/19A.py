import sys
input = sys.stdin.readline

n = int(input())

teams = [input().strip() for _ in range(n)]

# stats: points, goal_diff, goals_scored
stats = {team: [0, 0, 0] for team in teams}

# number of matches
m = n * (n - 1) // 2

for _ in range(m):
    line = input().strip()
    
    # split
    names, score = line.split()
    t1, t2 = names.split('-')
    g1, g2 = map(int, score.split(':'))
    
    # goals
    stats[t1][1] += g1 - g2
    stats[t2][1] += g2 - g1
    
    stats[t1][2] += g1
    stats[t2][2] += g2
    
    # points
    if g1 > g2:
        stats[t1][0] += 3
    elif g2 > g1:
        stats[t2][0] += 3
    else:
        stats[t1][0] += 1
        stats[t2][0] += 1

# sort teams by ranking rules
teams.sort(key=lambda x: (
    -stats[x][0],
    -stats[x][1],
    -stats[x][2]
))

# take top n//2
qualified = teams[:n//2]

# sort lexicographically
qualified.sort()

# output
for t in qualified:
    print(t)