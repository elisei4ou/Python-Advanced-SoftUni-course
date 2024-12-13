rows = int(input())
matrix = [[j for j in list(input())]for i in range(rows)]
searched_element = input()


for row_index in range(rows):
    for col_index in range(rows):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            exit()

else:
    print(f"{searched_element} does not occur in the matrix")