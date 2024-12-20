from tkinter import Button
from tkinter import Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from json import dump, loads
from buying_page import display_products


def get_user_data():
    info_data = []

    with open("db//users_information.txt") as user_file:
        for line in user_file:
            info_data.append(loads(line))

    return info_data


def render_entry():

    register_button = Button(
        root,
        text="Register",
        bg="white",
        fg="black",
        bd=2,
        width=8,
        height=2,
        command=register
    )

    login_button = Button(
        root,
        text="Login",
        bg="green",
        fg="white",
        bd=2,
        width=8,
        height=2,
        command=login
    )

    frame.create_window(365, 380, window=register_button)
    frame.create_window(435, 380, window=login_button)


def register():
    clean_screen()

    frame.create_text(340, 300, text="First Name: ")
    frame.create_text(340, 325, text="Last Name: ")
    frame.create_text(340, 350, text="Username: ")
    frame.create_text(340, 375, text="Password: ")

    frame.create_window(440, 300, window=first_name_box)
    frame.create_window(440, 325, window=last_name_box)
    frame.create_window(440, 350, window=username_box)
    frame.create_window(440, 375, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="white",
        fg="black",
        width=8,
        height=1,
        command=registration,
    )

    frame.create_window(410, 420, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", "a") as users_file:
            info_dict["Password"] = get_password_hash(info_dict["Password"])
            dump(info_dict, users_file)
            users_file.write("\n")
            display_products()


def check_registration(info_dict):
    frame.delete("error")

    for key, value in info_dict.items():
        if not value.strip():
            frame.create_text(
                410,
                395,
                text=f"{key}, cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

    users_data = get_user_data()

    for user in users_data:
        if user["Username"] == info_dict["Username"]:
            frame.create_text(
                410,
                395,
                text=f'Username: \'{user["Username"]}\' is already taken',
                fill="red",
                tags="error",
            )

            return False

    return True


def login():
    clean_screen()

    frame.create_text(340, 325, text="Username: ")
    frame.create_text(340, 350, text="Password: ")

    frame.create_window(440, 325, window=username_box)
    frame.create_window(440, 350, window=password_box)

    frame.create_window(410, 400, window=login_button)


def logging():

    if check_login():
        display_products()
    else:
        frame.create_text(
            410,
            375,
            text=f'Incorrect username or password!',
            fill="red",
            tags="error",
        )


def check_login():
    users_data = get_user_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break
    else:
        login_button["state"] = "normal"


login_button = Button(
    root,
    text="Login",
    bg="green",
    fg="white",
    width=8,
    height=1,
    command=logging
)


login_button['state'] = 'disabled'
root.bind("<KeyRelease>", change_login_button_status)

first_name_box = Entry(root)
last_name_box = Entry(root)
username_box = Entry(root)
password_box = Entry(root, show="*")
