def even_odd(*args):
    odd_numbers = []
    even_numbers = []
    for number in args[:len(args) - 1]:
        number = int(number)

        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    if args[-1] == "odd":
        return odd_numbers
    else:
        return even_numbers


print(even_odd(1, 2, 3, 4, 5, 6, "even"))