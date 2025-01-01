from collections import deque

size = int(input())
list_with_moves = deque(move for move in input().split(", "))

field = []
squirrel_position = []
collected_hazelnut = 0
needed_hazelnut = 3
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
killed = False

for r in range(size):
    col = list(input())
    field.append(col)

    if "s" in col:
        squirrel_position = [r, col.index("s")]
        field[squirrel_position[0]][squirrel_position[1]] = "*"

for move in list_with_moves:

    next_row = moves[move][0] + squirrel_position[0]
    next_col = moves[move][1] + squirrel_position[1]

    if not 0 <= next_row < size or not 0 <= next_col < size:
        print("The squirrel is out of the field.")
        killed = True
        break

    squirrel_position = [next_row, next_col]
    squirrel_next_move = field[next_row][next_col]

    if squirrel_next_move == "h":
        collected_hazelnut += 1
        field[next_row][next_col] = "*"

        if collected_hazelnut == needed_hazelnut:
            break

    elif squirrel_next_move == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        killed = True
        break

if collected_hazelnut < needed_hazelnut and not killed:
    print("There are more hazelnuts to collect.")

elif collected_hazelnut == needed_hazelnut and not killed:
    print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {collected_hazelnut}")





