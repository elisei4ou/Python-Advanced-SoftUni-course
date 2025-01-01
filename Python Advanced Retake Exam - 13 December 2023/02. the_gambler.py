size = int(input())

board = []
gambler_position = ()
amount = 100
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    current_row = list(input())
    board.append(current_row)

    if "G" in current_row:

        gambler_position = [row, current_row.index("G")]
        board[row][current_row.index("G")] = "-"


while True:
    command = input()

    if command == "end":
        print(f"End of the game. Total amount: {amount}$")
        board[gambler_position[0]][gambler_position[1]] = "G"
        [print("".join(row))for row in board]
        break

    gambler_position = (gambler_position[0] + moves[command][0], gambler_position[1] + moves[command][1])
    gambler_row = gambler_position[0]
    gambler_col = gambler_position[1]

    if not 0 <= gambler_row < size and 0 <= gambler_col < size:
        print("Game over! You lost everything!")
        break

    current_place = board[gambler_row][gambler_col]

    if current_place == "-":
        continue

    elif current_place == "W":
        amount += 100

    elif current_place == "P":
        amount -= 200

    elif current_place == "J":
        amount += 100000
        board[gambler_row][gambler_col] = "-"
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {amount}$")
        board[gambler_position[0]][gambler_position[1]] = "G"
        [print("".join(row)) for row in board]
        break

    board[gambler_row][gambler_col] = "-"

    if amount <= 0:
        print("Game over! You lost everything!")
        break
