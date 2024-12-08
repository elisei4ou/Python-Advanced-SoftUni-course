from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

presents = {150: "Doll",
            250: "Wooden train",
            300: "Teddy bear",
            400: "Bicycle"}

successful_task = [{"Doll", "Wooden train"}, {"Teddy bear", "Bicycle"}]

crafted_presents = []
crafted_presents_as_set = set()
crafted_presents_as_dict = {}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    total_magic_level = current_material * current_magic_level

    if total_magic_level in presents:
        crafted_presents.append(presents[total_magic_level])
    elif total_magic_level < 0:
        materials.append(current_material + current_magic_level)
    elif total_magic_level > 0:
        materials.append(current_material + 15)
    else:
        if current_material > 0:
            materials.append(current_material)
        if current_magic_level > 0:
            magic_levels.appendleft(current_magic_level)

crafted_presents_as_set = set(crafted_presents)

for p in successful_task:
    if p.issubset(crafted_presents_as_set):
        print("The presents are crafted! Merry Christmas!")
        break
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present in crafted_presents:
    if present not in crafted_presents_as_dict:
        crafted_presents_as_dict[present] = 0
    crafted_presents_as_dict[present] += 1

for p, c in sorted(crafted_presents_as_dict.items()):
    print(f"{p}: {c}", end="\n")






