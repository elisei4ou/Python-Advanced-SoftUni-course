from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude = 0
reached_top = True

for i in range(1, len(fuel_needed) + 1):

    altitude += 1

    current_fuel = initial_fuel.pop()
    current_index = additional_consumption_index.popleft()
    current_fuel_need = fuel_needed.popleft()

    if current_fuel - current_index >= current_fuel_need:
        print(f"John has reached: Altitude {altitude}")\

    else:
        print(f"John did not reach: Altitude {altitude}")
        altitude -= 1
        reached_top = False
        break

if reached_top:
    print("John has reached all the altitudes and managed to reach the top!")

if not reached_top and altitude > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: " + f"{', '.join([f'Altitude {a}'for a in range(1, altitude + 1)])}")


elif not reached_top and altitude == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")