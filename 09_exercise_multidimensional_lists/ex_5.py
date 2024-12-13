rows, columns = [int(i) for i in input().split()]

first_and_last_element = 97
middle_element = 97
matrix = []

for row_index in range(rows):
    sub_list = []
    for col_index in range(columns):
        first_el = chr(first_and_last_element + row_index)
        second_el = chr(middle_element + row_index + col_index)
        third_el = first_el
        our_el = first_el + second_el + third_el
        sub_list.append(our_el)
    matrix.append(sub_list)


[print(*r) for r in matrix]
