rows, columns = [int(i) for i in input().split()]
field = []
my_position = []
my_first_position = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for r in range(rows):
    c = list(input())
    field.append(c)

    if "B" in c:
        my_position = [r, c.index("B")]
        my_first_position = my_position

while True:
    command = input()

    next_r = my_position[0] + moves[command][0]
    next_c = my_position[1] + moves[command][1]

    if not 0 <= next_r < rows or not 0 <= next_c < columns:
        print("The delivery is late. Order is canceled.")
        field[my_first_position[0]][my_first_position[1]] = " "
        break

    if field[next_r][next_c] == "*":
        continue

    elif field[next_r][next_c] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        field[next_r][next_c] = "R"

    elif field[next_r][next_c] == "A":
        print("Pizza is delivered on time! Next order...")
        field[next_r][next_c] = "P"
        break

    elif field[next_r][next_c] == "-":
        field[next_r][next_c] = "."

    my_position = [next_r, next_c]

[print("".join(r)) for r in field]
