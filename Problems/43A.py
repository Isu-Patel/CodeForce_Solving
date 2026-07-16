n = int(input())

goals = {}

for _ in range(n):
    team = input().strip()
    goals[team] = goals.get(team , 0) + 1

winner = max(goals, key=goals.get)
print(winner)