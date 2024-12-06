from collections import deque

commands = int(input())
all_pumps = deque()
all_distance = deque()
tracker = 0
current_fuel = 0
the_pump = 0

for every_command in range(commands):
    info = input().split()
    amount_of_petrol, distance = int(info[0]), int(info[1])
    all_pumps.append(amount_of_petrol)
    all_distance.append(distance)

while True:
    current_distance = all_distance[tracker]
    current_pump = all_pumps[tracker]
    current_fuel += current_pump

    if current_fuel >= current_distance:
        current_fuel -= current_distance
        tracker += 1

    else:
        all_distance.append(all_distance.popleft())
        all_pumps.append(all_pumps.popleft())
        tracker = 0
        the_pump += 1
        current_fuel = 0

    if tracker == commands:
        break


print(the_pump)