n = int(input())
odd_numbers = set()
even_numbers = set()

for z in range(1, n + 1):
    name = input()

    current_name_sum = 0
    for char in name:
        current_name_sum += ord(char)
    current_name_sum = current_name_sum // z

    if current_name_sum % 2 == 0:
        even_numbers.add(current_name_sum)
    else:
        odd_numbers.add(current_name_sum)

if sum(odd_numbers) == sum(even_numbers):
    union = odd_numbers.union(even_numbers)
    print(*union, sep=", ")

elif sum(odd_numbers) > sum(even_numbers):
    difference = odd_numbers.difference(even_numbers)
    print(*difference, sep=", ")

else:
    symmetric_difference = odd_numbers.symmetric_difference(even_numbers)
    print(*symmetric_difference, sep=", ")
