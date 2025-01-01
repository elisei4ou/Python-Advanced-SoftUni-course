from collections import deque


def check_sum(present):
    if 100 <= present < 200:
        return "Gemstone"
    elif 200 <= present < 300:
        return "Porcelain Sculpture"
    elif 300 <= present < 400:
        return "Gold"
    elif 400 <= present < 500:
        return "Diamond Jewellery"
    else:
        return False


materials = [int(el) for el in input().split()]
magics = deque(int(el) for el in input().split())

crafted_presents = {"Gemstone": 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}

while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    present = material + magic

    result = check_sum(present)
    if result:
        crafted_presents[result] += 1

    elif present < 100:
        if present % 2 == 0:
            material *= 2
            magic *= 3
            present = material + magic

            result = check_sum(present)
            if result:
                crafted_presents[result] += 1

        else:
            material *= 2
            magic *= 2
            present = material + magic

            result = check_sum(present)
            if result:
                crafted_presents[result] += 1

    elif present >= 500:
        material //= 2
        magic //= 2
        present = material + magic

        result = check_sum(present)
        if result:
            crafted_presents[result] += 1

if crafted_presents["Gemstone"] > 0 and crafted_presents["Porcelain Sculpture"] > 0:
    print("The wedding presents are made!")
elif crafted_presents["Gold"] > 0 and crafted_presents["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(el) for el in materials])}")
if magics:
    print(f"Magic left: {', '.join([str(el) for el in magics])}")

for gift, quantity in sorted(crafted_presents.items()):
    if quantity > 0:
        print(f"{gift}: {quantity}")





