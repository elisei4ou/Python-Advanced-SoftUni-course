rows = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for row_index in range(rows):
    current_row = [int(i) for i in input().split(', ')]
    matrix.append(current_row)
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][rows - (row_index + 1)])

print(f"Primary diagonal: {', '.join([str(n) for n in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(n) for n in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

