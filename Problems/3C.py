board = [input().strip() for _ in range(3)]

x = sum(row.count('X') for row in board)
o = sum(row.count('0') for row in board)

def win(p):
    for i in range(3):
        if all(board[i][j] == p for j in range(3)):
            return True
        if all(board[j][i] == p for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == p:
        return True
    if board[0][2] == board[1][1] == board[2][0] == p:
        return True
    return False

xwin = win('X')
owin = win('0')

# illegal checks
if o > x or x > o + 1:
    print("illegal")
elif xwin and owin:
    print("illegal")
elif xwin and x != o + 1:
    print("illegal")
elif owin and x != o:
    print("illegal")
elif xwin:
    print("the first player won")
elif owin:
    print("the second player won")
elif x + o == 9:
    print("draw")
elif x == o:
    print("first")
else:
    print("second")