rows, columns = [int(i) for i in input().split()]

matrix = []
my_position = []
other_players_count = 3
found_players = 0
moves_made = 0

for row in range(rows):
    col = list(input().split())
    matrix.append(col)

    if "B" in col:
        my_position = [row, col.index("B")]
        matrix[my_position[0]][my_position[1]] = "-"

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "Finish":
        break

    next_row = my_position[0] + moves[command][0]
    next_col = my_position[1] + moves[command][1]

    if not 0 <= next_row < rows or not 0 <= next_col < columns:
        continue

    elif matrix[next_row][next_col] == "O":
        continue

    my_position = [next_row, next_col]
    next_position_on_field = matrix[next_row][next_col]
    moves_made += 1

    if next_position_on_field == "P":
        found_players += 1
        matrix[next_row][next_col] = "-"

        if found_players == other_players_count:
            break

print("Game over!")
print(f"Touched opponents: {found_players} Moves made: {moves_made}")

