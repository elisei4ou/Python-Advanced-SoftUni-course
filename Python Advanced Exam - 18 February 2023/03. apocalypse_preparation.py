from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

created_items = {}

while textiles and medicaments:

    current_textile = textiles.popleft()
    current_med = medicaments.pop()
    created_item = current_textile + current_med

    if created_item == 30:
        if "Patch"  not in created_items.keys():
            created_items["Patch"] = 0
        created_items["Patch"] += 1

    elif created_item == 40:
        if "Bandage" not in created_items.keys():
            created_items["Bandage"] = 0
        created_items["Bandage"] += 1

    elif created_item == 100:
        if "MedKit" not in created_items.keys():
            created_items["MedKit"] = 0
        created_items["MedKit"] += 1

    elif created_item > 100:
        if "MedKit" not in created_items.keys():
            created_items["MedKit"] = 0
        created_items["MedKit"] += 1

        remaining_sum = created_item - 100
        medicaments[-1] += remaining_sum

    else:
        current_med += 10
        medicaments.append(current_med)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item, amount in created_items:
    print(f"{item} - {amount}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")




