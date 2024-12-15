def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


def power(n1, n2):
    return n1 ** n2


def calculation(sign, n1, n2):
    return signs[sign](n1, n2)


signs = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "^": power,
}