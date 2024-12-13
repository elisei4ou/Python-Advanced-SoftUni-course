from collections import deque

quantity_of_food = int(input())
each_order = deque(int(x) for x in input().split())

print(max(each_order))

for z in range(len(each_order)):
    current_food = each_order.popleft()

    if quantity_of_food < current_food:
        each_order.appendleft(current_food)
        print(f"Orders left: {' '.join(str(x) for x in each_order)}")
        break

    quantity_of_food -= current_food

else:
    print("Orders complete")


