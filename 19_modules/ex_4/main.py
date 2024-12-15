from operations import calculation


some_input = input().split()
number_1 = float(some_input[0])
sign = some_input[1]
number_2 = int(some_input[2])


result = calculation(sign, number_1, number_2)
print(f"{result:.2f}")

