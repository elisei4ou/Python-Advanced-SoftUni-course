from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0

while chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_milk_cup = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_milk_cup <= 0:
        continue

    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk_cup)
        continue

    if current_milk_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk_cup:
        milkshakes += 1

    else:
        cups_of_milk.append(current_milk_cup)
        chocolates.append(current_chocolate - 5)

    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
        break

else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")



