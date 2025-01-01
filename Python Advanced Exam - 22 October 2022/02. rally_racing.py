size = int(input())
racing_number = input()

car = [0, 0]
km_passed = 0

matrix = [[col for col in input().split()]for row in range(size)]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == 'End':
        print(f"Racing car {racing_number} DNF.")
        break

    car_next_row = car[0] + moves[command][0]
    car_next_col = car[1] + moves[command][1]
    car = [car_next_row, car_next_col]
    car_next_position = matrix[car_next_row][car_next_col]

    if car_next_position == ".":
        km_passed += 10

    elif car_next_position == "T":
        first_t_coordinates = [car_next_row, car_next_col]

        for r in range(size):
            for c in range(size):
                if matrix[r][c] == "T":
                    if r != first_t_coordinates[0] or c != first_t_coordinates[1]:
                        car = [r, c]
                        km_passed += 30
                        break

        matrix[car_next_row][car_next_col] = "."
        matrix[car[0]][car[1]] = "."

    elif car_next_position == "F":
        km_passed += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
print(f"Distance covered {km_passed} km.")
matrix[car[0]][car[1]] = "C"

[print(''.join(r))for r in matrix]


