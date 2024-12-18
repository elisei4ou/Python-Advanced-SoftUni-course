def binary_search(target, numbers):
    left_idx = 0
    right_idx = len(numbers) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2

        if numbers[mid_idx] == target:
            return mid_idx
        elif numbers[mid_idx] > target:
            right_idx = mid_idx - 1
        elif numbers[mid_idx] < target:
            left_idx = mid_idx + 1

    return -1


nums = [int(x) for x in input().split()]
searched_num = int(input())

print(binary_search(searched_num, nums))
