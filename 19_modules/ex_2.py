from pyfiglet import figlet_format


def figlet_form(text):
    return figlet_format(text)


some_text = input()
print(figlet_form(some_text))
