def shopping_cart(*args):
    my_products = {"Dessert": [], "Soup": [], "Pizza": []}
    result = ""
    current_limit = 0

    for x in args:
        if x == "Stop":
            break

        type_meal, product = x[0], x[1]
        if type_meal == "Soup":
            current_limit = 3
        elif type_meal == "Pizza":
            current_limit = 4
        elif type_meal == "Dessert":
            current_limit = 2

        if product not in my_products[type_meal] and len(my_products[type_meal]) < current_limit:
            my_products[type_meal].append(product)

    my_products = sorted(my_products.items(), key=lambda x: (-len(x[1]), x[0]))

    if current_limit:
        for meal, prod in my_products:
            result += f"{meal}:\n"

            for p in sorted(prod):
                result += f" - {p}\n"

    else:
        result += "No products in the cart!"

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))



