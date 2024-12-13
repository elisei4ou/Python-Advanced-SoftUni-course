def check_valid_index(current_row, current_col):
    if 0 <= current_row < rows and 0 <= current_col < rows:
        return True


def check_for_trap(row, col):
    if matrix[row][col] == "X":
        return True


rows = int(input())
matrix = []
bunny_position = []
bunny_first_position = []
max_bunny_path = []
direction = ""
current_eggs = float('-inf')

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for every_row in range(rows):
    every_col = input().split()
    matrix.append(every_col)

    if "B" in every_col:
        bunny_first_position = [every_row, every_col.index("B")]

for every_direction, coordinates in moves.items():
    bunny_current_eggs = 0
    bunny_position = bunny_first_position
    bunny_path = []

    while True:
        bunny_next_row = bunny_position[0] + coordinates[0]
        bunny_next_col = bunny_position[1] + coordinates[1]

        if not check_valid_index(bunny_next_row, bunny_next_col):
            break
        if check_for_trap(bunny_next_row, bunny_next_col):
            break

        bunny_current_eggs += int(matrix[bunny_next_row][bunny_next_col])
        bunny_position = [bunny_next_row, bunny_next_col]
        bunny_path.append([bunny_next_row, bunny_next_col])

    if bunny_current_eggs >= current_eggs:
        current_eggs = bunny_current_eggs
        max_bunny_path = bunny_path
        direction = every_direction

print(direction)
[print(x) for x in max_bunny_path]
print(current_eggs)
