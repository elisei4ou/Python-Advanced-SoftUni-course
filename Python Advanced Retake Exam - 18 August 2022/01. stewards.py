from collections import deque

seats = input().split(", ")
first_sequence = deque(int(el) for el in input().split(", "))
second_sequence = deque(int(el) for el in input().split(", "))

taken_seat = []
seat_matches = 0

for i in range(1, 11):
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()

    current_char = chr(first_num + second_num)

    first_seat = str(first_num) + current_char
    second_seat = str(second_num) + current_char

    if first_seat in seats:
        seats.remove(first_seat)
        taken_seat.append(first_seat)
        seat_matches += 1

    elif second_seat in seats:
        seats.remove(second_seat)
        taken_seat.append(second_seat)
        seat_matches += 1

    else:
        first_sequence.append(first_num)
        second_sequence.appendleft(second_num)

    if seat_matches == 3:
        break


print(f"Seat matches: {', '.join(taken_seat)}")
print(f"Rotations count: {i}")