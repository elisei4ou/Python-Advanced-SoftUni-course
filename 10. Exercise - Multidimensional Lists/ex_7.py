presents = int(input())
rows = int(input())
field = []
santa_position = []
nice_kids = 0
kids_with_presents = 0
is_all_nice_kids_got_present = False
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for every_row in range(rows):
    current_row = input().split()
    field.append(current_row)

    if "S" in current_row:
        santa_position = [every_row, current_row.index("S")]
        field[santa_position[0]][santa_position[1]] = "-"

    nice_kids += current_row.count("V")

command = input()

while command != "Christmas morning":
    next_row = moves[command][0] + santa_position[0]
    next_col = moves[command][1] + santa_position[1]
    santa_position = [next_row, next_col]

    if field[next_row][next_col] == "V":
        presents -= 1
        kids_with_presents += 1
        field[next_row][next_col] = "-"

        if kids_with_presents == nice_kids:
            is_all_nice_kids_got_present = True

        elif presents == 0:
            print(f"Santa ran out of presents!")
            break

    elif field[next_row][next_col] == "X":
        field[next_row][next_col] = "-"

    elif field[next_row][next_col] == "C":
        field[next_row][next_col] = "-"
        for movement, coordinates in moves.items():
            santa_next_row = next_row + coordinates[0]
            santa_next_col = next_col + coordinates[1]

            if field[santa_next_row][santa_next_col] == "V":
                presents -= 1
                kids_with_presents += 1
                field[santa_next_row][santa_next_col] = "-"

                if kids_with_presents == nice_kids:
                    is_all_nice_kids_got_present = True

                elif presents == 0:
                    print(f"Santa ran out of presents!")
                    break

            elif field[santa_next_row][santa_next_col] == "X":
                presents -= 1
                field[santa_next_row][santa_next_col] = "-"

                if presents == 0:
                    print(f"Santa ran out of presents!")
                    break

    if presents == 0:
        break

    command = input()

field[santa_position[0]][santa_position[1]] = "S"
[print(*x) for x in field]
if is_all_nice_kids_got_present:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - kids_with_presents} nice kid/s.")
