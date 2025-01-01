def going_throw_direction(board, way, current_el, cur_r, cur_c):
    count = 0
    for i in range(1, 4):
        board_next_row = cur_r + way[0] * i
        board_next_col = cur_c + way[1] * i
        if 0 <= board_next_col < COLUMNS:
            if board[board_next_row][board_next_col] == current_el:
                count += 1
            else:
                break
        else:
            break
    return count


def going_throw_other_direction(board, way, current_el, cur_r, cur_c):
    count = 0
    for i in range(1, 4):
        board_next_row = cur_r - way[0] * i
        board_next_col = cur_c - way[1] * i
        if 0 <= board_next_col < COLUMNS:
            if board[board_next_row][board_next_col] == current_el:
                count += 1
            else:
                break
        else:
            break
    return count


def is_winner(board, searched_el):
    for direction in directions:
        first_count = going_throw_direction(board, direction, player, row, col)
        second_count = going_throw_other_direction(board, direction, player, row, col)
        if first_count + second_count + 1 >= 4:
            return True
    else:
        return False


def player_choose(board, col):
    for r in range(-1, -ROWS - 1, -1):
        if board[r][col] == 0:
            return r, col



ROWS = 6
COLUMNS = 7

board = [[0 for c in range(COLUMNS)]for r in range(ROWS)]

turns = 0
directions = (
    (0, -1),
    (-1, 0),
    (-1, -1),
    (+1, -1)
)
while True:
    player = 1 if turns % 2 == 0 else 2

    try:
        column = int(input(f"Player {player}, please choose a column: "))
        if 0 <= column - 1 <= len(board):
            column = column - 1
        else:
            print("Please choose a valid index!")
            continue
        row, col = player_choose(board, column)
        board[row][col] = player
        if is_winner(board, player):
            [print(row) for row in board]
            print(f"The winner is {player}")
            break
        turns += 1
        [print(row)for row in board]

    except ValueError:
       print("Please choose a valid index!")
