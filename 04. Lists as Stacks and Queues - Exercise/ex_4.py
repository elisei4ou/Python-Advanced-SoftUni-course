clothes = list((int(x) for x in input().split()))
capacity = int(input())
full_space = 0
racks = 0

while clothes:
    current_piece = clothes.pop()
    full_space += current_piece

    if full_space > capacity:
        clothes.append(current_piece)
        racks += 1
        full_space = 0

    elif full_space == capacity:
        racks += 1
        full_space = 0

if full_space:
    print(racks + 1)
else:
    print(racks)

