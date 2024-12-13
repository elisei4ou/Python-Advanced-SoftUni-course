rows, columns = [int(i) for i in input().split()]
matrix = [[c for c in input().split()]for r in range(rows)]
command, *coordinates = input().split()

while command != "END":
    if command != "swap":
        print("Invalid input!")
        command, *coordinates = input().split()
        continue

    elif len(coordinates) != 4:
        print("Invalid input!")
        command, *coordinates = input().split()
        continue

    first_coordinate = [int(coordinates[0]), int(coordinates[1])]
    second_coordinate = [int(coordinates[2]), int(coordinates[3])]

    if 0 > first_coordinate[0] or first_coordinate[0] > rows:
        print("Invalid input!")
        command, *coordinates = input().split()
        continue
    elif 0 > first_coordinate[1] or first_coordinate[1] > rows:
        print("Invalid input!")
        command, *coordinates = input().split()
        continue
    elif 0 > second_coordinate[0] or second_coordinate[0] > rows:
        print("Invalid input!")
        command, *coordinates = input().split()
        continue
    elif 0 > second_coordinate[1] or second_coordinate[1] > rows:
        print("Invalid input!")
        command, *coordinates = input().split()
        continue

    matrix[first_coordinate[0]][first_coordinate[1]], matrix[second_coordinate[0]][second_coordinate[1]] = \
    matrix[second_coordinate[0]][second_coordinate[1]], matrix[first_coordinate[0]][first_coordinate[1]]

    [print(*j) for j in matrix]

    command, *coordinates = input().split()