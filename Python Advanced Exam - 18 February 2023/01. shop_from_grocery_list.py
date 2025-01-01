def shop_from_grocery_list(budget, products, *args):
    bought_products = []
    result = ""

    for every_product, price in args:

        if every_product in products and every_product not in bought_products:
            if budget >= price:
                bought_products.append(every_product)
                budget -= price

            else:
                break

    if len(bought_products) == len(products):
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."

    else:
        result += f"You did not buy all the products. Missing products: {', '.join([p for p in products if p not in bought_products])}."

    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

