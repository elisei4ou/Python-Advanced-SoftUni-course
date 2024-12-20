from helpers import clean_screen
from json import load, dump
from PIL import ImageTk, Image
from canvas import frame
from tkinter import Button
from canvas import root


def display_products():
    clean_screen()
    display_stock()


def display_stock():
    with open("db//products.json", "r") as stock:
        info = load(stock)

    x, y = 250, 20

    for item_name, item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info["image"]))
        images.append(item_img)

        frame.create_text(x, y, text=item_name, font=("Courier", 20))
        frame.create_image(x, y + 140, image=item_img)

        if item_info["quantity"] > 0:
            color = "green"
            text = f"In stock: {item_info['quantity']}"

            item_button = Button(
                root,
                text="Buy",
                bg="blue",
                fg="white",
                font=("Comic Sans MS", 12),
                width=6,
                command=lambda x=item_name, y=info: buy_product(x, y)
            )

            frame.create_window(x, y + 295, window=item_button)

        else:
            color = "red"
            text = f"Out of stock"

        frame.create_text(
            x,
            y + 265,
            text=text,
            fill=color,
            font=("arabic", 14)
        )

        x += 300
        if x >= 700:
            y += 350
            x = 250


def buy_product(product_name, info):
    info[product_name]["quantity"] -= 1

    with open("db/products.json", "w") as stock:
        dump(info, stock)

    display_products()



images = []