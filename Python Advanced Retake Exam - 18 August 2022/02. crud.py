SIZE = 6

matrix = [[col for col in input().split()]for row in range(SIZE)]
my_position = [int(el) for el in input() if el.isdigit()]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input().split(", ")

    if command[0] == "Stop":
        break

    instruction = command[0]
    direction = command[1]

    next_row = my_position[0] + moves[direction][0]
    next_col = my_position[1] + moves[direction][1]
    matrix_next_position = matrix[next_row][next_col]
    my_position = [next_row, next_col]

    if instruction == "Create":
        value = command[2]

        if matrix_next_position == ".":
            matrix[next_row][next_col] = value

    elif instruction == "Update":
        value = command[2]

        if matrix_next_position != ".":
            matrix[next_row][next_col] = value

    elif instruction == "Delete":
        matrix[next_row][next_col] = "."

    elif instruction == "Read":

        if matrix_next_position != ".":
            print(matrix_next_position)

[print(' '.join(row))for row in matrix]