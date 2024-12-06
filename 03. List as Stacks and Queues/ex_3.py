from collections import deque

name = input()
line_with_people = deque()

while name != "End":
    if name == "Paid":
        while line_with_people:
            print(line_with_people.popleft())
    else:
        line_with_people.append(name)
    name = input()

print(f"{len(line_with_people)} people remaining.")