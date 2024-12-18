def bubble_sort(numbers):
    idx = 0
    is_sorted = False

    while not is_sorted:
        is_sorted = True

        for i in range(1, len(numbers) - idx):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
                is_sorted = False

        idx += 1

    return numbers


nums = [int(x) for x in input().split()]
print(*bubble_sort(nums))