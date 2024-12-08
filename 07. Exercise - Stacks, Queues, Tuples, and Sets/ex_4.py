from collections import deque

working_bees = deque(int(x) for x in input().split())
all_nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())

collected_honey = 0

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if a > 0 else 0
}

while all_nectar and working_bees:
    current_bee = working_bees.popleft()
    current_nectar = all_nectar.pop()

    if current_nectar >= current_bee:
        our_symbol = symbols.popleft()
        collected_honey += abs(functions[our_symbol](current_bee, current_nectar))

    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {collected_honey}")

if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if all_nectar:
    print(f"Nectar left: {', '.join(str(x) for x in all_nectar)}")
