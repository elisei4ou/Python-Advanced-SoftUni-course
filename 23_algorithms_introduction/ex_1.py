def sum_of_nums(numbers: list, idx=0):
    if idx + 1 == len(numbers):
        return numbers[idx]

    return numbers[idx] + sum_of_nums(numbers, idx+1)


numbers = [int(x) for x in input().split()]
print(sum_of_nums(numbers))