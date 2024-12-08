from collections import deque

some_text = deque(input().split())
all_colours = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
how_colours_made = {"orange": ['red', 'yellow'],
                    'purple': ['red', 'blue'],
                    'green': ['yellow', 'blue']}
found_colours = []

while some_text:
    first_substring = some_text.popleft()
    second_substring = some_text.pop() if some_text else ""

    for x in (first_substring + second_substring, second_substring + first_substring):
        if x in all_colours:
            found_colours.append(x)
            break

    else:
        for el in (first_substring[:-1], second_substring[:-1]):
            if el:
                some_text.insert(len(some_text)//2, el)


for colour, parts in how_colours_made.items():
    if colour in found_colours:
        if parts[0] not in found_colours or parts[1] not in found_colours:
            found_colours.remove(colour)

print(found_colours)