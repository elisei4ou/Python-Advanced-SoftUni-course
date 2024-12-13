from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_liters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup > current_bottle:
        current_cup -= current_bottle
        cups.appendleft(current_cup)
    else:
        wasted_liters += current_bottle - current_cup

if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
else:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")

print(f"Wasted litters of water: {wasted_liters}")