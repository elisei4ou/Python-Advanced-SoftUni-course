size = int(input())

battlefield = []
submarine = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
possible_hits = 3
taken_hits = 0
battle_cruisers = 3
hit_cruisers = 0

for row in range(size):
    col = list(input())

    battlefield.append(col)

    try:
        submarine = [row, col.index("S")]
        battlefield[submarine[0]][submarine[1]] = "-"
    except ValueError:
        pass

while True:
    command = input()

    next_row = moves[command][0] + submarine[0]
    next_col = moves[command][1] + submarine[1]
    submarine = [next_row, next_col]
    current_position_on_field = battlefield[submarine[0]][submarine[1]]

    if current_position_on_field == "*":
        battlefield[next_row][next_col] = "-"
        taken_hits += 1

        if taken_hits == possible_hits:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine[0]}, {submarine[1]}]!")
            break

    elif current_position_on_field == "C":
        battlefield[next_row][next_col] = "-"
        hit_cruisers += 1

        if hit_cruisers == battle_cruisers:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

battlefield[submarine[0]][submarine[1]] = "S"

for every_row in battlefield:
    print("".join(every_row))