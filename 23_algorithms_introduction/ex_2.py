def recursive_factorial(num: int):
    if num == 1:
        return 1

    return num * recursive_factorial(num-1)


number = int(input())
print(recursive_factorial(number))