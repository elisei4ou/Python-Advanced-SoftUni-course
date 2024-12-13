rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(j) for j in input().split()] for x in range(rows)]

for every_col in range(columns):
    current_column_sum = 0
    for every_row in range(rows):
        current_column_sum += matrix[every_row][every_col]

    print(current_column_sum)