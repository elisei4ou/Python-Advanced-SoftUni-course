def words_sorting(*args):
    words = {}
    result = ""

    for word in args:
        ascii_sum = 0

        for char in word:
            ascii_sum += ord(char)
        words[word] = ascii_sum

    if sum(words.values()) % 2 == 0:
        words = sorted(words.items(), key=lambda x: x[0])
    elif sum(words.values()) % 2 != 0:
        words = sorted(words.items(), key=lambda x: -x[1])

    for word, ascii_sum in words:
        result += f"{word} - {ascii_sum}\n"

    return result

print(
    words_sorting(
        'cacophony',
        '',
  ))


