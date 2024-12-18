def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        pi = i - 1

        while pi >= 0 and numbers[pi] > key:
            numbers[pi + 1] = numbers[pi]
            pi -= 1

        numbers[pi + 1] = key

    return numbers


nums = [int(x) for x in input().split()]
print(*insertion_sort(nums))
