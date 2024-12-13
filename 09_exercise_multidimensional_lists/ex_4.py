

rows, columns = [int(i) for i in input().split()]
matrix = [[int(c) for c in input().split()]for r in range(rows)]

positions = {
    'up left': [-1, -1],
    'up': [-1, 0],
    'up right': [-1, +1],
    'left': [0, -1],
    'current': [0, 0],
    'right': [0, +1],
    'down left': [+1, -1],
    'down': [+1, 0],
    'down right': [+1, +1],
}
max_sum = float("-inf")
max_matrix = []
current_matrix = []

for row_index in range(1, rows - 1):
    for col_index in range(1, columns - 1):
        current_sum = 0
        current_matrix = []
        index = 0
        for every_position, indexes in positions.items():
            current_element = matrix[row_index + indexes[0]][col_index + indexes[1]]
            current_sum += current_element
            current_matrix.append(current_element)

        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

print(f"Sum = {max_sum}")
max_matrix = [max_matrix[i:i + 3] for i in range(0, len(max_matrix), 3)]
[print(*r) for r in max_matrix]


