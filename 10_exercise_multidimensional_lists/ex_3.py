def check_valid_index(current_row, current_col):
    if 0 <= current_row < rows and 0 <= current_col < rows:
        return True


def find_killed_knights(k_r, k_c):
    killed_knights = 0
    for every_possible_position in knight_moves:
        next_row = k_r + every_possible_position[0]
        next_col = k_c + every_possible_position[1]
        if check_valid_index(next_row, next_col):
            if matrix[next_row][next_col] == "K":
                killed_knights += 1

    return killed_knights


rows = int(input())
matrix = [[c for c in list(input())]for r in range(rows)]

knight_moves = {
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1)
}

knight_with_most_attacks = []
is_there_attacks = True
removed_knights = 0

while is_there_attacks:
    most_attacks = 0
    knight_with_most_attacks = []

    for every_row in range(rows):
        for every_col in range(rows):

            if matrix[every_row][every_col] == "K":
                current_killed_knights = find_killed_knights(every_row, every_col)
                if most_attacks < current_killed_knights:
                    knight_with_most_attacks = [every_row, every_col]
                    most_attacks = current_killed_knights

    if most_attacks:
        matrix[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = "0"
        removed_knights += 1
    else:
        is_there_attacks = False

print(removed_knights)
