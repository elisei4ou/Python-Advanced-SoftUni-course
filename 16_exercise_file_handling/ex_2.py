import string

letters = []
marks = []
index = 0

with open("text1.txt") as file:
    text = file.readlines()

for row in text:
    index += 1
    current_letters = 0
    current_marks = 0

    for char in row:
        if char.isalpha():
            current_letters += 1
        elif char in string.punctuation:
            current_marks += 1

    with open("output.txt", "a") as file:
        file.write(f"Line {index}: {row.strip()} ({current_letters})({current_marks})\n")
