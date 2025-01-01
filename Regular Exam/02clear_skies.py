SIZE = int(input())

matrix = []
jetfighter = []
armour = 300
all_enemy = 4
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    col = list(input())
    matrix.append(col)

    if "J" in col:
        jetfighter = [row, col.index("J")]
        matrix[jetfighter[0]][jetfighter[1]] = "-"

while True:
    command = input()

    next_row = jetfighter[0] + moves[command][0]
    next_col = jetfighter[1] + moves[command][1]
    jet_next_position = matrix[next_row][next_col]
    jetfighter = [next_row, next_col]

    if jet_next_position == "E":
        matrix[next_row][next_col] = "-"
        all_enemy -= 1

        if all_enemy == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            armour -= 100

            if armour == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                break

    elif jet_next_position == "R":
        matrix[next_row][next_col] = "-"
        armour = 300

matrix[jetfighter[0]][jetfighter[1]] = "J"
[print(''.join(r)) for r in matrix]









