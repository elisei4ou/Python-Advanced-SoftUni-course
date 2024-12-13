from collections import deque

green_light_duration = int(input())
current_time = green_light_duration
free_window = int(input())
cars = deque()
passed_cars = 0
current_passed_cars = 0
crash = False

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars} total cars passed the crossroads.")
        break

    if command != "green":
        cars.append(command)

    elif command == "green":
        while current_time > 0 and cars:
            current_car = cars.popleft()

            if len(current_car) > current_time + free_window:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[current_time+free_window]}.")
                raise SystemExit

            passed_cars += 1
            current_time -= len(current_car)

        current_time = green_light_duration

