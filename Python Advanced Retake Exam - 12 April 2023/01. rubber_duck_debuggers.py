from collections import deque

time_for_tasks = deque(int(i) for i in input().split())
number_of_tasks = [int(i) for i in input().split()]

ducks = {"darth_vader_ducky": 0, "thor_ducky": 0, "big_blue_rubber_ducky": 0, "small_yellow_rubber_ducky": 0}

while time_for_tasks and number_of_tasks:
    current_time = time_for_tasks.popleft()
    current_task = number_of_tasks.pop()

    duck = current_time * current_task

    if 0 <= duck <= 60:
        ducks["darth_vader_ducky"] += 1

    elif 61 <= duck <= 120:
        ducks["thor_ducky"] += 1

    elif 121 <= duck <= 180:
        ducks["big_blue_rubber_ducky"] += 1

    elif 181 <= duck <= 240:
        ducks["small_yellow_rubber_ducky"] += 1

    else:
        current_task -= 2

        number_of_tasks.append(current_task)
        time_for_tasks.append(current_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['darth_vader_ducky']}")
print(f"Thor Ducky: {ducks['thor_ducky']}")
print(f"Big Blue Rubber Ducky: {ducks['big_blue_rubber_ducky']}")
print(f"Small Yellow Rubber Ducky: {ducks['small_yellow_rubber_ducky']}")