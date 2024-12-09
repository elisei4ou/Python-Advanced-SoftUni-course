rows = int(input())

matrix = []
sub_list = []

for every_row in range(rows):
    sub_list = [int(i) for i in input().split(', ') if int(i) % 2 == 0]
    matrix.append(sub_list)

print(matrix)



