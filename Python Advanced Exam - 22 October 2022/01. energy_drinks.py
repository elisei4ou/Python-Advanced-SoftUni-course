from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

starting_caffeine = 0
maximum_caffeine = 300

while milligrams_of_caffeine and energy_drinks:

    current_milligrams = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    result = current_milligrams * current_energy_drink

    if starting_caffeine + result <= maximum_caffeine:
        starting_caffeine += result

    else:
        energy_drinks.append(current_energy_drink)

        if starting_caffeine - 30 >= 0:
            starting_caffeine -= 30

        else:
            starting_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(drink) for drink in energy_drinks])}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {starting_caffeine} mg caffeine.")



