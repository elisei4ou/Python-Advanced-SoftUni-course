from collections import deque

string_expression = deque(input().split())
current_numbers = []

for every_num in string_expression:

    if every_num == "*":
        sums = 1
        for n in current_numbers:
            sums = sums * n
        current_numbers = [sums]

    elif every_num == "+":
        sums = 0
        for n in current_numbers:
            sums = sums + n
        current_numbers = [sums]

    elif every_num == "-":
        sums = current_numbers[0]
        for n in current_numbers[1::]:
            sums = sums - n
        current_numbers = [sums]

    elif every_num == "/":
        sums = current_numbers[0]
        for n in current_numbers[1::]:
            sums = int(sums / n)
        current_numbers = [sums]

    else:
        current_numbers.append(int(every_num))

print(*current_numbers)
