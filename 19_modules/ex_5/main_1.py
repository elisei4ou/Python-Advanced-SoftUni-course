from body import create_fibonacci, locate_number


def start_program():
    command = input().split()
    sequence = []

    while command[0] != "Stop":

        if command[0] == "Create":
            count = int(command[2])
            sequence = create_fibonacci(count)
            print(*sequence)

        elif command[0] == "Locate":
            number = int(command[1])
            try:
                result = locate_number(number, sequence)
                print(result)
            except NameError:
                print("There is no given sequence")

        command = input().split()


start_program()