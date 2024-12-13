rows = int(input())

list_with_numbers = []
for every_row in range(rows):

    list_with_numbers.extend([int(i) for i in input().split(', ')])

print(list_with_numbers)