def gather_credits(num_credits, *args):
    enrolled_courses = []
    collected_points = 0
    result = ""

    for course, points in args:

        if course not in enrolled_courses:
            if num_credits > 0:
                enrolled_courses.append(course)
                num_credits -= points
                collected_points += points

                if num_credits <= 0:
                    break

    if num_credits <= 0:
        result += f"Enrollment finished! Maximum credits: {collected_points}.\n"
        result += f"Courses: {', '.join(sorted(enrolled_courses))}"

    else:
        result += f"You need to enroll in more courses! You have to gather {num_credits} credits more."

    return result

print(gather_credits(
    80,
    ("Basics", 27),
))








