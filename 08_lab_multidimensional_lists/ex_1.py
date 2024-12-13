rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sum_of_all = 0

for every_row in range(rows):
    current_row = [int(i) for i in input().split(", ")]
    matrix.append(current_row)
    sum_of_all += sum(current_row)

print(sum_of_all)
print(matrix)