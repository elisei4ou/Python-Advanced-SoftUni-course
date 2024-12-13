from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar = [int(nec) for nec in input().split()]
symbols = deque(input().split())

total_honey = 0

operations = {
    "+": lambda x: current_bee + current_nectar,
    "-": lambda x: current_bee - current_nectar,
    "*": lambda x: current_bee * current_nectar,
    "/": lambda x: abs(current_bee / current_nectar) if current_nectar > 0 else 0
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        if current_symbol == "+":
            total_honey += current_bee + current_nectar
        elif current_symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey += current_bee * current_nectar
        elif current_symbol == "/":
            total_honey += abs(current_bee / current_nectar)
#total_honey += operations[current_symbol](current_bee, current_nectar)

    else:
        bees.appendleft(current_bee)

print(total_honey)