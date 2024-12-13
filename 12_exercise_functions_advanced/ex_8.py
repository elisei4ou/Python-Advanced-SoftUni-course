def age_assignment(*names, **kwargs):
    result = ""
    for name in sorted(names):
        for char, age in kwargs.items():
            if char == name[0]:
                result += f"{name} is {age} years old.\n"

    return result


print(age_assignment("Peter", "George", G=26, P=19))