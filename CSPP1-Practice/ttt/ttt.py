def is_valid(board):
    x_sum = 0
    o_sum = 0
    sum_val = 0
    for i in board:
        x_sum += i.count('x')
        o_sum += i. count('o')
        sum_val += i.count('x') + i. count('o') + i.count('.')
    if sum_val != 9:
        print("invalid input")
        return
    if (x_sum - o_sum not in (0, 1, -1)):
        return ("invalid game")
    return True

def check_game(board):
    count = 0
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            count += 1
    for i in range(len(board)):
        if board[0][1] == board[1][i] and board[1][i] == board[2][i]:
            count += 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        count += 1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        count += 1
    if count > 1:
        print ("invalid game")
    else:
        return True

def is_horizontal(board):
    count = 0
    tmp = ''
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            count += 1
            tmp = board[i][0]
    if (count > 1):
        return None
    else:
        return tmp

def is_vertical(board):
    count = 0
    tmp = ''
    for i in range(len(board)):
        if board[0][1] == board[1][i] and board[1][i] == board[2][i]:
            count += 1
            tmp = board[0][i]
    if (count > 1):
        return None
    else:
        return tmp

def is_diagonal(board):
    count = 0
    tmp = ''
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            count += 1
            tmp = board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            count += 1
            tmp = board[0][2]
    if (count > 1):
        return None
    else:
        return tmp 

def check_winner(board):
    flag = 0
    winner = is_horizontal(board)
    winner1 = is_vertical(board)
    winner2 = is_diagonal(board)

    if (winner and winner1) or (winner1 and winner2) or (winner and winner2):
        return ("invalid game")
    if winner:
        return winner
    if winner1:
        return winner1
    if winner2:
        return winner2
    else:
        return "draw"

def main():
    board = []

    for _ in range(3):
        board.append(input().split())
    if is_valid(board) and check_game(board):
        print(check_winner(board))

main()
