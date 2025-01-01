size = int(input())

area = []
my_position = []
fish_collected = 0
drown = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):

    col = list(input())
    area.append(col)
    if "S" in col:
        my_position = (row, col.index("S"))
        area[my_position[0]][my_position[1]] = "-"

while True:

    command = input()
    if command == "collect the nets":
        break

    my_position = [my_position[0] + moves[command][0], my_position[1] + moves[command][1]]

    if 0 <= my_position[0] < size or 0 <= my_position[1] < size:
        for i in range(2):
            if my_position[i] < 0:
                my_position[i] = size - 1
            elif my_position[i] >= size:
                my_position[i] = 0

    if area[my_position[0]][my_position[1]].isdigit():
        fish_collected += int(area[my_position[0]][my_position[1]])
        area[my_position[0]][my_position[1]] = "-"

    elif area[my_position[0]][my_position[1]] == "W":
        my_position_as_str = f"[{my_position[0]},{my_position[1]}]"
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: {my_position_as_str}")
        drown = True
        break

if not drown:
    area[my_position[0]][my_position[1]] = "S"

    if fish_collected >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(
            f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_collected} tons of fish more.")

    if fish_collected > 0:
        print(f"Amount of fish caught: {fish_collected} tons.")

    [print(''.join(r)) for r in area]
