file_name = "numbers.txt"
result = 0

with open(file_name) as file:
    for number in file:
        result += int(number[0])  #number.strip does the same job

print(result)
