from collections import deque

SIZE = 8
board = []
white_pawn = []
black_pawn = []

for row in range(SIZE):
    col = input().split()
    board.append(col)

    if "w" in col:
        white_pawn = [row, col.index("w")]
    if "b" in col:
        black_pawn = [row, col.index("b")]

white_and_black = deque(["w", "b"])
which_position = []

while True:

    if white_and_black[0] == "w":
        next_row = white_pawn[0] - 1
        next_col = white_pawn[1]
        take_left_col = white_pawn[1] - 1
        take_right_col = white_pawn[1] + 1

        board[white_pawn[0]][white_pawn[1]] = "-"

        if 0 > next_row:
            which_position = [str(chr(97 + white_pawn[1])), "8"]
            print(f"Game over! White pawn is promoted to a queen at {''.join(which_position)}.")
            break
        if take_left_col >= 0:
            if board[next_row][take_left_col] == "b":
                white_pawn = [next_row, take_left_col]
                which_position = [str(chr(97 + take_left_col)), str(SIZE - next_row)]
                print(f"Game over! White win, capture on {''.join(which_position)}.")
                break
        if take_right_col < SIZE:
            if board[next_row][take_right_col] == "b":
                white_pawn = [next_row, take_right_col]
                which_position = [str(chr(97 + take_right_col)), str(SIZE - next_row)]
                print(f"Game over! White win, capture on {''.join(which_position)}.")
                break

        board[next_row][next_col] = "w"
        white_pawn = [next_row, next_col]

    elif white_and_black[0] == "b":
        next_row = black_pawn[0] + 1
        next_col = black_pawn[1]
        take_left_col = black_pawn[1] - 1
        take_right_col = black_pawn[1] + 1

        board[black_pawn[0]][black_pawn[1]] = "-"

        if 8 <= next_row:
            which_position = [str(chr(97 + black_pawn[1])), "1"]
            print(f"Game over! Black pawn is promoted to a queen at {''.join(which_position)}.")
            break
        if take_left_col >= 0:
            if board[next_row][take_left_col] == "w":
                black_pawn = [next_row, take_left_col]
                which_position = [str(chr(97 + take_left_col)), str(SIZE - next_row)]
                print(f"Game over! Black win, capture on {''.join(which_position)}.")
                break
        if take_right_col < SIZE:
            if board[next_row][take_right_col] == "w":
                black_pawn = [next_row, take_right_col]
                which_position = [str(chr(97 + take_right_col)), str(SIZE - next_row)]
                print(f"Game over! Black win, capture on {''.join(which_position)}.")
                break

        board[next_row][next_col] = "b"
        black_pawn = [next_row, next_col]

    white_and_black.rotate(1)
