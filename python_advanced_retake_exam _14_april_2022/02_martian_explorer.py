def check_position(curr_row, curr_col):
    if curr_row >= SIZE:
        curr_row = 0
    elif curr_row < 0:
        curr_row = SIZE - 1
    elif curr_col >= SIZE:
        curr_col = 0
    elif curr_col < 0:
        curr_col = SIZE - 1

    return curr_row, curr_col


SIZE = 6
matrix = []
rover_position = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for row in range(SIZE):
    col = input().split()
    matrix.append(col)

    if "E" in col:
        rover_position = [row, col.index("E")]
        matrix[row][col.index("E")] = "-"

commands = [c for c in input().split(", ")]

for command in commands:
    next_row = rover_position[0] + moves[command][0]
    next_col = rover_position[1] + moves[command][1]

    next_row, next_col = check_position(next_row, next_col)
    symbol_on_matrix = matrix[next_row][next_col]
    rover_position = [next_row, next_col]

    if symbol_on_matrix == "W":
        water_deposit += 1
        print(f"Water deposit found at ({next_row}, {next_col})")

    elif symbol_on_matrix == "M":
        print(f"Metal deposit found at ({next_row}, {next_col})")
        metal_deposit += 1

    elif symbol_on_matrix == "C":
        print(f"Concrete deposit found at ({next_row}, {next_col})")
        concrete_deposit += 1

    elif symbol_on_matrix == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

if water_deposit and metal_deposit and concrete_deposit:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
