class ValueCannotBeNegative(Exception):
    pass


for n in range(5):
    i = int(input())
    if i < 0:
        raise ValueCannotBeNegative
