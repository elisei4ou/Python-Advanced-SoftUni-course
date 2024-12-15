def create_fibonacci(count):
    fibonacci_nums = [0, 1]

    for i in range(count - 2):
        next_fibonacci = fibonacci_nums[-1] + fibonacci_nums[-2]
        fibonacci_nums.append(next_fibonacci)

    return fibonacci_nums


def locate_number(number, sequence):
    try:
        index = sequence.index(number)
        return f"The number - {number} is at index {index}"

    except ValueError:
        return f"The number {number} is not in the sequence"
