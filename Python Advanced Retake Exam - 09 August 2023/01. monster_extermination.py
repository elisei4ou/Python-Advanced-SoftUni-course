from collections import deque

armour_of_monsters = deque(int(x) for x in input().split(","))
strength_strikes = [int(x) for x in input().split(",")]

starting_monster = len(armour_of_monsters)

while armour_of_monsters and strength_strikes:

    current_monster = armour_of_monsters.popleft()
    current_strike = strength_strikes.pop()

    if current_strike > current_monster:
        remained_strike = current_strike - current_monster
        if strength_strikes:
            strength_strikes[-1] += remained_strike
        else:
            strength_strikes.append(remained_strike)

    elif current_monster > current_strike:
        current_monster -= current_strike
        armour_of_monsters.append(current_monster)

if not armour_of_monsters:
    print("All monsters have been killed!")

if not strength_strikes:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {starting_monster - len(armour_of_monsters)}")