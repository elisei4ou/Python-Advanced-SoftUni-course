import re

words_name = "words.txt"
text_name = "text.txt"

searched_words = ""
list_with_searched_words = []
text = ""
dict_for_words = {}


with open(words_name) as file:
    for word in file:
        searched_words += word.strip()
    list_with_searched_words = searched_words.split(" ")

with open(text_name) as file:
    for word in file:
        text += word.lower()

for every_word in list_with_searched_words:
    pattern = rf"\b{every_word}\b"
    count_per_word = re.findall(pattern, text)
    dict_for_words[every_word] = len(count_per_word)

sorted_dict = sorted(dict_for_words.items(), key=lambda x: -x[1])

with open("output.txt", "a") as file:
    for w in sorted_dict:
        file.write(f"{w[0]} - {w[1]}\n")

