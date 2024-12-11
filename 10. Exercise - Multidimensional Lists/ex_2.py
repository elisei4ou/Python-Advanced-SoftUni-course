def check_index(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True


rows = int(input())
matrix = [[int(c)for c in input().split()]for row in range(rows)]
command = input().split()

while command[0] != "END":
    instruction, current_row, current_col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if check_index(current_row, current_col):
        if instruction == "Add":
            matrix[current_row][current_col] += value
        if instruction == "Subtract":
            matrix[current_row][current_col] -= value

    else:
        print("Invalid coordinates")

    command = input().split()

[print(*r) for r in matrix]
