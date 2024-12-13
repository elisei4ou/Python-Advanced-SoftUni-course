def check_index(row_index, col_index, rows):
    if 0 > row_index or row_index >= rows:
        return False
    if 0 > col_index or col_index >= rows:
        return False
    else:
        return True

rows = int(input())
commands = input().split()
field = []
miner_position = []
all_coals = 0
collected_coals = 0

for r in range(rows):
    column = input().split()
    field.append(column)
    if 's' in column:
        miner_position = [r, column.index("s")]
        field[miner_position[0]][miner_position[1]] = "*"
    if "c" in column:
        all_coals += column.count("c")

possible_commands = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0],
}

for every_command in commands:
    next_row = possible_commands[every_command][0] + miner_position[0]
    next_col = possible_commands[every_command][1] + miner_position[1]

    if check_index(next_row, next_col, rows):
        miner_position = [next_row, next_col]

        if field[next_row][next_col] == "c":
            collected_coals += 1
            field[next_row][next_col] = "*"
            if collected_coals == all_coals:
                print(f"You collected all coal! ({next_row}, {next_col})")
                break

        if field[next_row][next_col] == "e":
            print(f"Game over! ({next_row}, {next_col})")
            break

else:
    print(f"{all_coals - collected_coals} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")





