gestures = [
    input().strip(),
    input().strip(),
    input().strip()
]

# gesture -> the gesture it beats
beats = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

players = ["F", "M", "S"]

winner = []

for i in range(3):
    if beats[gestures[i]] == gestures[(i + 1) % 3] and \
       beats[gestures[i]] == gestures[(i + 2) % 3]:
        winner.append(players[i])

if len(winner) == 1:
    print(winner[0])
else:
    print("?")