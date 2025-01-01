def students_credits(*args):
    all_credits = 0
    dict_with_courses = {}
    result = ""

    for x in args:
        course_name, credit, max_text_points, diyans_points = x.split("-")

        current_get_credit = int(credit) / int(max_text_points) * int(diyans_points)
        dict_with_courses[course_name] = current_get_credit
        all_credits += current_get_credit

    if all_credits >= 240:
        result += f"Diyan gets a diploma with {all_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - all_credits:.1f} credits more for a diploma.\n"

    dict_with_courses = sorted(dict_with_courses.items(), key=lambda x: -x[1])

    for course, points in dict_with_courses:
        result += f"{course} - {points:.1f}\n"

    return result

print(
    students_credits(
        "Computer Science-12-300-0",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)





