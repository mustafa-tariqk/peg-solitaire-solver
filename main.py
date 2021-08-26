import random

def pick_spot(x, y):
    begin_x = random.randint(0, x-1)
    if begin_x == 0 or begin_x == x-1:
        begin_y = random.randint(1, y-2)
    else:
        begin_y = random.randint(0, y-1)

    return [begin_x, begin_y]


def make_board(x, y):
    board = []
    for i in range(x):
        board.append([])

        if i == 0 or i == x-1:
            board[i].append(None)
            for j in range(1, y-1):
                board[i].append(True)
            board[i].append(None)

        else:
            for j in range(y):
                board[i].append(True)

    spot = pick_spot(x, y)
    board[spot[0]][spot[1]] = False
    return board


def find_empties(board):
    empties = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == False:
                empties.append([i, j])
    return empties


def check(board, x, y):
    board_x = len(board)
    board_y = len(board[0])

    if x - 1 < 0 or x + 1 > board_x:
        return False
    if y - 1 < 0 or y + 1 > board_y:
        return False

    if board[x][y] == None or board[x][y] == False:
        return False

    return True


def check_up(board, x, y):
    return check(board, x, y - 1) and check(board, x, y - 2)


def check_down(board, x, y):
    return check(board, x, y + 1) and check(board, x, y + 2)


def check_left(board, x, y):
    return check(board, x - 1, y) and check(board, x - 2, y)


def check_right(board, x, y):
    return check(board, x + 1, y) and check(board, x + 2, y)


def move_up(board, x, y):
    move = board[:]
    move[x][y] = True
    move[x][y-1] = False
    move[x][y-2] = False
    return move


def move_down(board, x, y):
    move = board[:]
    move[x][y] = True
    move[x][y+1] = False
    move[x][y+2] = False
    return move


def move_left(board, x, y):
    move = board[:]
    move[x][y] = True
    move[x-1][y] = False
    move[x-2][y] = False
    return move


def move_right(board, x, y):
    move = board[:]
    move[x][y] = True
    move[x+1][y] = False
    move[x+2][y] = False
    return move


def is_finished(board):
    board_x = len(board)
    board_y = len(board[0])

    if len(find_empties(board)) == board_x * board_y - 5:
        return True
    return False


def is_stuck(board):
    empties = find_empties(board)
    for empty in empties:
        if check_up(board, empty[0], empty[1]) or check_down(board, empty[0], empty[1]) or check_left(board, empty[0], empty[1]) or check_right(board, empty[0], empty[1]):
            return False
    return True


def is_possible(board):

    empties = find_empties(board)

    for empty in empties:
        if check_up(board, empty[0], empty[1]):
            move = move_up(board, empty[0], empty[1])
            print(is_stuck(move))
            is_possible(move)

        if check_down(board, empty[0], empty[1]):
            move = move_down(board, empty[0], empty[1])
            print(is_stuck(move))
            is_possible(move)

        if check_left(board, empty[0], empty[1]):
            move = move_left(board, empty[0], empty[1])
            print(is_stuck(move))
            is_possible(move)

        if check_right(board, empty[0], empty[1]):
            move = move_right(board, empty[0], empty[1])
            print(is_stuck(move))
            is_possible(move)


if __name__ == "__main__":
    print(is_possible(make_board(5, 5)))
