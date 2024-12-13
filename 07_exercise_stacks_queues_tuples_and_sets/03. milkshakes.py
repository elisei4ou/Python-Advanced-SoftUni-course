from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and cups_of_milk:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue

    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)

    elif cup_of_milk <= 0:
        chocolates.append(chocolate)

    elif chocolate == cup_of_milk:
        milkshakes += 1

    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

    if milkshakes == 5:
        print(f"Great! You made all the chocolate milkshakes needed!")
        break

else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x)for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x)for x in cups_of_milk])}")
else:
    print("Milk: empty")
