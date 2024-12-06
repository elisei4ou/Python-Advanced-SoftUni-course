from collections import deque

some_input = deque(input())

opening_brackets = "([{"
closing_brackets = ")]}"
my_brackets = deque()

while some_input:
    current_brackets = some_input.popleft()

    if current_brackets in opening_brackets:
        my_brackets.append(current_brackets)
    elif not my_brackets:
        print("NO")
        break
    else:
        if f"{my_brackets.pop() + current_brackets}" not in "(){}[]":
            print("NO")
            break

else:
    print("YES")