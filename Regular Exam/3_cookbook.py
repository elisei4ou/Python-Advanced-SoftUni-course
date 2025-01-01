def cookbook(*args):
    the_cookbook = {}
    result = ""

    for dishes, cuisine, ingredients in args:
        if cuisine not in the_cookbook.keys():
            the_cookbook[cuisine] = {dishes: ingredients}
        the_cookbook[cuisine].update({dishes: ingredients})

    the_cookbook = sorted(the_cookbook.items(), key=lambda x: (-len(x[1]), x[0]))

    for key, value in the_cookbook:
        result += f"{key} cuisine contains {len(value)} recipes:\n"
        for dish, ingr in sorted(value.items()):
            result += f"  * {dish} -> Ingredients: {', '.join(ingr)}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
