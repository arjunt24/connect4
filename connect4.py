def print_board(board):
    print("")
    for y in range(len(board[0])-1, -1, -1):
        for x in range(len(board)):
            print(board[x][y], end = " ")
        print("")
    for x in range(1,len(board)+1):
        print(x, end = " ")
    print("\n")


def place(board, move, c):
    for i in range(6):
        if board[move][i] == 'o':
            board[move][i] = c
            return board

def check_win(board, c):
    # check verticals
    if sum([c*4 in "".join(col) for col in board]) > 0:
        return True
    # check horizontals
    if sum([c*4 in "".join(col) for col in [[board[y][x] for y in range(7)] for x in range(6)]]) > 0:
        return True
    # check northwest diagonals
    if sum([c*4 in "".join(col) for col in [[board[(k-5)*(k>5)+d][(5-k)*(k<5)+d] for d in range(k+1 if k<6 else 12-k)] for k in range(3,9)]]) > 0:
        return True
    # check northeast diagonals
    if sum([c*4 in "".join(col) for col in [[board[6 - (k-5)*(k>5)-d][(5-k)*(k<6)+d] for d in range(k+1 if k<6 else 12-k)] for k in range(3,9)]]) > 0:
        return True


# board = [[str(i)+str(j) for i in range(6)] for j in range(7)]
board = [['o' for i in range(6)] for j in range(7)]
print_board(board)
cur_player = True
while True:
    prompt = "Enter move for Player " + '1'*cur_player + '2'*(not cur_player) + ": "
    move = input(prompt).strip()
    try:
        move = int(move) - 1
    except:
        print("Illegal input")
        continue
    if move not in range(7):
        print("Illegal number")
        continue
    if board[move][5] != 'o':
        print("Column full")
        continue

    board = place(board, move, 'r'*cur_player + 'y'*(not cur_player))
    print_board(board)
    if check_win(board, 'r'*cur_player + 'y'*(not cur_player)):
        print("Player ", '1'*cur_player + '2'*(not cur_player) , " wins!", sep="")
        break

    cur_player = not cur_player
