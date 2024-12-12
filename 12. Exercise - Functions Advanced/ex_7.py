def grocery_store(**kwargs):
    result = ""
    sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for products in sorted_products:
        result += f"{products[0]}: {products[1]}\n"
    return result


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

