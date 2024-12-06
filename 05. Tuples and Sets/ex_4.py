n = int(input())
parking_lot = set()

for _ in range(n):
    direction, car = input().split(", ")
    if direction == "IN":
        parking_lot.add(car)

    elif direction == "OUT":
        if car in parking_lot:
            parking_lot.remove(car)

if parking_lot:
    [print(c) for c in parking_lot]
else:
    print("Parking Lot is Empty")