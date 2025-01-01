def start_spring(**kwargs):
    spring_objects = {}
    result = ""

    for object, type in kwargs.items():
        if type not in spring_objects.keys():
            spring_objects[type] = []
        spring_objects[type].append(object)

    spring_objects = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))

    for type, objects in spring_objects:
        result += f"{type}:\n"

        for object in sorted(objects):
            result += f"-{object}\n"

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
