from collections import deque

some_input = deque(input().split())

colors = ["red", "blue", "yellow", "orange", "purple", "green"]
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"blue", "yellow"}
}
made_colors = []
my_secondary_colors = []
while some_input:
    first_word = some_input.popleft()
    second_word = some_input.pop() if some_input else ""
    for word in (first_word + second_word, second_word + first_word):
        if word in colors:
            made_colors.append(word)
            break

    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                some_input.insert(len(some_input)//2, el)


for color in set(secondary_colors.keys()).intersection(made_colors):
    if not secondary_colors[color].issubset(made_colors):
        made_colors.remove(color)

print(made_colors)