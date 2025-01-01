from collections import deque

eggs_size = deque(int(el) for el in input().split(", "))
papers_size = [int(el) for el in input().split(", ")]

box_size = 50
boxes = 0

while eggs_size and papers_size:
    egg = eggs_size.popleft()
    paper = papers_size.pop()

    if egg <= 0:
        papers_size.append(paper)
        continue

    if egg == 13:
        papers_size.append(paper)
        papers_size[0], papers_size[-1] = papers_size[-1], papers_size[0]
        continue

    wrapped_egg = egg + paper

    if wrapped_egg <= box_size:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")

else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs_size:
    print(f"Eggs left: {', '.join([str(egg) for egg in eggs_size])}")

if papers_size:
    print(f"Pieces of paper left: {', '.join([str(p) for p in papers_size])}")

