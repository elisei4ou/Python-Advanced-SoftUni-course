def check_index(row_index, col_index, rows, columns):
    if 0 > row_index or row_index >= rows:
        return False
    if 0 > col_index or col_index >= columns:
        return False
    else:
        return True


rows, columns = [int(i) for i in input().split()]
field = []
player_position = []
player_winning_positions = []
is_dead = False
is_won = False

possible_commands = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0],
}

for every_row in range(rows):
    column = list(input())
    field.append(column)
    if "P" in column:
        player_position = [every_row, column.index("P")]
        field[player_position[0]][player_position[1]] = "."

commands = list(input())

for every_command in commands:
    next_row = possible_commands[every_command][0] + player_position[0]
    next_col = possible_commands[every_command][1] + player_position[1]
    player_previous_positions = [player_position[0], player_position[1]]
    player_position = [next_row, next_col]

    if not check_index(next_row, next_col, rows, columns):
        player_winning_positions = player_previous_positions
        player_position = player_previous_positions
        is_won = True

    if field[player_position[0]][player_position[1]] == "B":
        player_winning_positions = player_position
        is_dead = True

    bunnies_positions = []

    for every_row_index in range(rows):
        for every_col_index in range(columns):

            if field[every_row_index][every_col_index] == "B":

                for way, coordinates in possible_commands.items():
                    next_bunny_row = every_row_index + coordinates[0]
                    next_bunny_col = every_col_index + coordinates[1]

                    if check_index(next_bunny_row, next_bunny_col, rows, columns):
                        bunnies_positions.append([next_bunny_row, next_bunny_col])

    for b in bunnies_positions:
        if [b[0], b[1]] == player_position:
            if not is_won:
                is_dead = True
                player_winning_positions = player_position
        field[b[0]][b[1]] = "B"

    if is_dead:
        break

    if is_won:
        break


[print(''.join(r))for r in field]
if is_dead:
    print(f"dead: {player_winning_positions[0]} {player_winning_positions[1]}")
if is_won:
    print(f"won: {player_winning_positions[0]} {player_winning_positions[1]}")




