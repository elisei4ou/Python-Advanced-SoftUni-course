rows, columns = [int(i) for i in input().split(', ')]

matrix = [[int(c) for c in input().split(', ')]for r in range(rows)]
max_sum = 0
small_matrix = []

for row_index in range(rows-1):
    for col_index in range(columns-1):
        current_index = matrix[row_index][col_index]
        right_index = matrix[row_index][col_index + 1]
        down_index = matrix[row_index + 1][col_index]
        diagonal_index = matrix[row_index + 1][col_index + 1]

        current_sum = current_index + right_index + down_index + diagonal_index

        if current_sum > max_sum:
            max_sum = current_sum
            small_matrix = [[current_index, right_index], [down_index, diagonal_index]]

[print(*j) for j in small_matrix]
print(max_sum)
