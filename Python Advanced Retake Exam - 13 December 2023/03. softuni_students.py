def softuni_students(*students, **courses):
    students_and_courses = {}
    invalid_courses = []

    result = ""

    for current_id, student_name in students:
        try:
            current_key = courses[current_id]
            students_and_courses[student_name] = current_key
        except KeyError:
            invalid_courses.append(student_name)

    students_and_courses = sorted(students_and_courses.items(), key=lambda x: x[0])
    invalid_courses = sorted(invalid_courses)

    if students_and_courses:
        for student, course in students_and_courses:
            result += f"*** A student with the username {student} has successfully finished the course {course}!\n"

    if invalid_courses:
        result += f"!!! Invalid course students: {', '.join(invalid_courses)}"

    return result


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
