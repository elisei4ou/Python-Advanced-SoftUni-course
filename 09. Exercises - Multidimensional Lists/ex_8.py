def check_index(row_index, col_index, length):
    if 0 > row_index or row_index > length:
        return False
    elif 0 > col_index or col_index > length:
        return False
    else:
        return True

rows = int(input())
matrix = [[int(c) for c in input().split()]for r in range(rows)]
bomb_coordinates = []
list_alive_cells = []


for sub_list in input().split():
    r, c = sub_list.split(",")
    r = int(r)
    c = int(c)
    bomb_coordinates.append([r, c])

positions = {
    'up left': [-1, -1],
    'up': [-1, 0],
    'up right': [-1, +1],
    'left': [0, -1],
    'right': [0, +1],
    'down left': [+1, -1],
    'down': [+1, 0],
    'down right': [+1, +1],
}

for every_bomb in bomb_coordinates:
    current_row_index = every_bomb[0]
    current_col_index = every_bomb[1]
    if matrix[current_row_index][current_col_index] > 0:
        bomb_value = matrix[current_row_index][current_col_index]
        matrix[current_row_index][current_col_index] = 0

        for every_bombed_place, coord in positions.items():
            current_bomb_row = coord[0] + current_row_index
            current_bomb_col = coord[1] + current_col_index

            if check_index(current_bomb_row, current_bomb_col, rows - 1):
                if matrix[current_bomb_row][current_bomb_col] <= 0:
                    continue
                else:
                    matrix[current_bomb_row][current_bomb_col] -= bomb_value

for r in matrix:
    for c in r:
        if c > 0:
            list_alive_cells.append(c)

print(f"Alive cells: {len(list_alive_cells)}")
print(f"Sum: {sum(list_alive_cells)}")
[print(*r) for r in matrix]





