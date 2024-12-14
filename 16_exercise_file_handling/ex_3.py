import os

command, *info = input().split("-")

while command != "End":

    if command == "Create":
        with open(f"{info[0]}", "w"):
            pass

    elif command == "Add":
        with open(f"{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{info[0]}", "r+") as file:
                file_as_text = file.read()
                current_info = info[1]
                file_info = info[2]
                file_as_text = file_as_text.replace(current_info, file_info)

                file.seek(0)
                file.write(file_as_text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"{info[0]}")
        except FileNotFoundError:
            print("An error occurred")

    command, *info = input().split("-")
