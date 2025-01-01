def accommodate_new_pets(capacity, weight_limit, *pets_info):

    accomodated_pets = {}
    result = ""

    for pet, weight in pets_info:

        if capacity > 0:
            if weight <= weight_limit:
                capacity -= 1
                try:
                    accomodated_pets[pet] += 1
                except KeyError:
                    accomodated_pets[pet] = 1
        else:
            result += "You did not manage to accommodate all pets!\n"
            break

    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"

    for pet_type, number in sorted(accomodated_pets.items()):
        result += f"{pet_type}: {number}\n"


    return result

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))




