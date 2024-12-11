def sorting_cheeses(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""

    for cheese, quantities in sorted_result:
        result += f"{cheese}\n"
        for x in sorted(quantities, reverse=True):
            result += f"{x}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
