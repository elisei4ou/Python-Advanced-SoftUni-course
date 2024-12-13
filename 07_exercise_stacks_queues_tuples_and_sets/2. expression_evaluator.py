from collections import deque
from math import floor

some_info = deque(input().split())
idx = 0

while len(some_info) > 1:
    if some_info[idx] == "+":
        for el in range(0, idx - 1):
            some_info.appendleft(int(some_info.popleft()) + int(some_info.popleft()))
    elif some_info[idx] == "-":
        for el in range(0, idx - 1):
            some_info.appendleft(int(some_info.popleft()) - int(some_info.popleft()))
    elif some_info[idx] == "*":
        for el in range(0, idx - 1):
            some_info.appendleft(int(some_info.popleft()) * int(some_info.popleft()))
    elif some_info[idx] == "/":
        for el in range(0, idx - 1):
            some_info.appendleft(floor(int(some_info.popleft()) / int(some_info.popleft())))

    if some_info[1] in "+-*/":
        del some_info[1]
        idx = 1

    idx += 1

print((some_info[0]))