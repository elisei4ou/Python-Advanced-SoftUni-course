from collections import deque

SIZE = 6
tom_and_jerry = deque(input().split(", "))
board = [[col for col in input().split()]for row in range(SIZE)]
is_tom_resting = False
is_jerry_resting = False
resting_character = ""

while True:
    current_player = tom_and_jerry[0]
    next_positions = [int(el) for el in input() if el.isdigit()]
    symbol = board[next_positions[0]][next_positions[1]]

    if is_tom_resting and current_player == "Tom":
        tom_and_jerry.rotate(-1)
        is_tom_resting = False
        continue

    if is_jerry_resting and current_player == "Jerry":
        tom_and_jerry.rotate(-1)
        is_jerry_resting = False
        continue

    if symbol == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif symbol == "T":
        print(f"{current_player} is out of the game! The winner is {tom_and_jerry[1]}.")
        break

    elif symbol == "W":
        print(f"{current_player} hits a wall and needs to rest.")

        if current_player == "Tom":
            is_tom_resting = True

        else:
            is_jerry_resting = True

    tom_and_jerry.rotate(-1)



