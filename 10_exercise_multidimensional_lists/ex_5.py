def check_index(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True


rows = int(input())
matrix = []
player_position = []
collected_teas = 0
needed_teas = 10

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for every_row in range(rows):
    current_row = input().split()
    matrix.append(current_row)

    if "A" in current_row:
        player_position = [every_row, current_row.index("A")]
        matrix[player_position[0]][player_position[1]] = "*"

while True:
    direction = input()
    next_row = player_position[0] + moves[direction][0]
    next_col = player_position[1] + moves[direction][1]

    if check_index(next_row, next_col):
        current_place = matrix[next_row][next_col]

        if current_place == "R":
            matrix[next_row][next_col] = '*'
            print("Alice didn't make it to the tea party.")
            break

        elif current_place.isdigit():
            collected_teas += int(current_place)

        player_position = [next_row, next_col]
        matrix[next_row][next_col] = '*'

        if collected_teas >= needed_teas:
            print("She did it! She went to the party.")
            break

    else:
        print("Alice didn't make it to the tea party.")
        break

[print(*x)for x in matrix]

