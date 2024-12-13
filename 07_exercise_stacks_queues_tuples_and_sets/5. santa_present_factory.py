from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

made_presents = []

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}
my_subsets = [{"Doll", "Wooden train"}, {"Teddy bear", "Bicycle"}]
while materials and magics:
    current_material = materials.pop()
    current_magic = magics.popleft()

    if current_material == 0 and current_magic == 0:
        continue

    elif current_material == 0:
        magics.appendleft(current_magic)
        continue

    elif current_magic == 0:
        materials.append(current_material)
        continue

    the_sum = current_material * current_magic
    if the_sum in presents.values():
        for every_present, sum in presents.items():
            if sum == the_sum:
                made_presents.append(every_present)
                break

    elif the_sum < 0:
        materials.append(current_material + current_magic)

    else:
        materials.append(current_material + 15)

for every_subset in my_subsets:
    if every_subset.issubset(made_presents):
        print("The presents are crafted! Merry Christmas!")
        break
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")

if magics:
    print(f"Magic left: {', '.join([str(x) for x in magics])}")

[print(f"{toy}: {made_presents.count(toy)}") for toy in sorted(set(made_presents))]