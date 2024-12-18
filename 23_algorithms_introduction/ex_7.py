def selection_sort(numbers):

    for i in range(len(numbers)):
        min_idx = i

        for current_index in range(i + 1, len(numbers)):
            if numbers[current_index] < numbers[min_idx]:
                min_idx = current_index

        numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]

    return numbers


nums = [int(x) for x in input().split()]
print(*selection_sort(nums))


