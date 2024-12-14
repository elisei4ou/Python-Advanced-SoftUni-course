punctuation = ("-", ",", ".", "!", "?")

with open("text1.txt") as file:
    text = file.readlines()

for n in range(0, len(text), 2):
    for every_punctuation in punctuation:
        if every_punctuation in text[n]:
            text[n] = text[n].replace(every_punctuation, "@")

    print(*text[n].split()[::-1])





