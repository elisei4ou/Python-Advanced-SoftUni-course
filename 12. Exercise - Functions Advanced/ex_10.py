def fill_the_box(*args):
    height = args[0]
    length = args[1]
    width = args[2]
    size_of_cube = height * length * width
    sum_of_cubes = 0

    for cube in args[3:]:
        if cube == "Finish":
            break
        sum_of_cubes += cube

    if size_of_cube >= sum_of_cubes:
        return f"There is free space in the box. You could put {size_of_cube - sum_of_cubes} more cubes."
    else:
        return f"No more free space! You have {sum_of_cubes - size_of_cube} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))