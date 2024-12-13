from collections import deque

water = int(input())
names = input()
line_with_people = deque()

while names != "Start":
    line_with_people.append(names)
    names = input()

command = input()
while command != "End":
    command = command.split()
    if len(command) == 1:
        current_person = line_with_people.popleft()
        current_litters = int(command[0])

        if water >= current_litters:
            print(f"{current_person} got water")
            water -= current_litters
        else:
            print(f"{current_person} must wait")

    elif len(command) == 2:
        water += int(command[1])

    command = input()

print(f"{water} liters left")

