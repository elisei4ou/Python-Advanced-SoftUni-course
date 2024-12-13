import copy
from collections import deque

rows, columns = [int(i) for i in input().split()]
word = deque(input())
word_copy = copy.deepcopy(word)

matrix = []

for row_index in range(rows):
    if row_index % 2 == 0:
        sub_list = []
        for col_index in range(columns):
            sub_list.append(word.popleft())
            if not word:
                for every_char in word_copy:
                    word.append(every_char)
        matrix.append(sub_list)

    else:
        sub_list = []
        for col_index in range(-1, -columns - 1, -1):
            sub_list.insert(col_index, word.popleft())
            if not word:
                for every_char in word_copy:
                    word.append(every_char)
        matrix.append(sub_list)

[print(''.join(r)) for r in matrix]
