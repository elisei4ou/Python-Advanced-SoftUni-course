rows, columns = [int(i) for i in input().split()]
matrix = [[c for c in input().split()]for r in range(rows)]

found_square_matrix = 0


for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_element = matrix[row_index][col_index]
        right_element = matrix[row_index][col_index + 1]
        lower_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        if current_element == right_element == lower_element == diagonal_element:
            found_square_matrix += 1

print(found_square_matrix)
