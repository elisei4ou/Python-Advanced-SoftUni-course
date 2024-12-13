sentence = input()
stack = []

for el in range(len(sentence)):
    if sentence[el] == "(":
        stack.append(el)
    elif sentence[el] == ")":
        print(sentence[stack.pop():el+1])