rows, columns = [int(i) for i in input().split(",")]

area = []
mouse_position = []
cheese_count = 0
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(rows):
    col = list(input())
    area.append(col)
    cheese_count += col.count("C")

    if "M" in col:
        mouse_position = [row, col.index("M")]
        area[mouse_position[0]][mouse_position[1]] = "*"


while True:
    command = input()

    if command == "danger":
        print("Mouse will come back later!")
        area[mouse_position[0]][mouse_position[1]] = "M"
        break

    next_row = mouse_position[0] + moves[command][0]
    next_col = mouse_position[1] + moves[command][1]

    if not 0 <= next_row < rows or not 0 <= next_col < columns:
        print("No more cheese for tonight!")
        area[mouse_position[0]][mouse_position[1]] = "M"
        break

    mouse_next_position = area[next_row][next_col]

    if mouse_next_position == "@":
        continue

    mouse_position = [next_row, next_col]

    if mouse_next_position == "C":
        area[next_row][next_col] = "*"
        cheese_count -= 1

        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            area[next_row][next_col] = "M"
            break

    elif mouse_next_position == "T":
        print("Mouse is trapped!")
        area[next_row][next_col] = "M"
        break

[print(''.join(r))for r in area]


