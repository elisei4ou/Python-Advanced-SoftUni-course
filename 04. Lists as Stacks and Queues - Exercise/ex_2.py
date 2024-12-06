n_commands = int(input())
stack_with_numbers = []

for c in range(n_commands):
    num = input().split()

    if num[0] == "1":
        stack_with_numbers.append(int(num[1]))

    if stack_with_numbers:
        if num[0] == "2":
            stack_with_numbers.pop()
        elif num[0] == "3":
            print(max(stack_with_numbers))
        elif num[0] == "4":
            print(min(stack_with_numbers))

if stack_with_numbers:
    print(", ".join(str(x) for x in stack_with_numbers[::-1]))