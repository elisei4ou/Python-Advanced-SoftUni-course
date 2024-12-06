from collections import deque
from datetime import datetime, timedelta

robots = {}
free_robots = deque()
all_products = deque()

for x in input().split(";"):
    robot_name, seconds = x.split("-")
    robots[robot_name] = [int(seconds), 0]

time = datetime.strptime(input(), "%H:%M:%S")

while True:
    product = input()

    if product == "End":
        break

    all_products.append(product)

while all_products:
    time += timedelta(0, 1)

    for name, info in robots.items():
        if info[1] != 0:
            robots[name][1] -= 1

        if info[1] == 0:
            free_robots.append(name)

    current_product = all_products.popleft()

    if free_robots:
        current_robot = free_robots.popleft()
        robots[current_robot][1] = robots[current_robot][0]

        print(f"{current_robot} - {current_product} [{time.strftime('%H:%M:%S')}]")
        free_robots = deque()

    else:
        all_products.append(current_product)



