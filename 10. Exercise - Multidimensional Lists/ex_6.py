def check_index(r, c):
    if 0 <= r < rows and 0 <= c < rows:
        return True


rows = 5
field = []
player_position = []
targets_positions = []
all_targets_count = 0
shot_targets = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    every_row = input().split()
    field.append(every_row)

    if "A" in every_row:
        player_position = [row, every_row.index("A")]
        field[player_position[0]][player_position[1]] = "."

    all_targets_count += every_row.count("x")

for every_command in range(int(input())):
    command = input().split()

    if command[0] == "move":
        direction, steps = command[1], int(command[2])
        next_row = []
        next_col = []

        if direction == "left" or direction == "right":
            next_row = moves[direction][0] + player_position[0]
            next_col = moves[direction][1] * steps + player_position[1]

        elif direction == "up" or direction == "down":
            next_row = moves[direction][0] * steps + player_position[0]
            next_col = moves[direction][1] + player_position[1]

        if check_index(next_row, next_col):
            if field[next_row][next_col] == ".":
                player_position = [next_row, next_col]

    elif command[0] == "shoot":
        direction = command[1]
        current_player_shot = player_position
        while True:
            next_shot_row = current_player_shot[0] + moves[direction][0]
            next_shot_col = current_player_shot[1] + moves[direction][1]

            if check_index(next_shot_row, next_shot_col):

                if field[next_shot_row][next_shot_col] == "x":
                    shot_targets += 1
                    field[next_shot_row][next_shot_col] = "."
                    targets_positions.append([next_shot_row, next_shot_col])

                    if shot_targets == all_targets_count:
                        print(f"Training completed! All {all_targets_count} targets hit.")
                        [print(x) for x in targets_positions]
                        exit()
                    break

                current_player_shot = [next_shot_row, next_shot_col]

            else:
                break

else:
    print(f"Training not completed! {all_targets_count - shot_targets} targets left.")

[print(x) for x in targets_positions]





