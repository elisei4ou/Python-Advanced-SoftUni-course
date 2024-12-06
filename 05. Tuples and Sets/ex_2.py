n = int(input())
all_students = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in all_students:
        all_students[name] = []
    all_students[name].append(grade)

for every_student, info in all_students.items():
    average_sum = sum(info)/len(info)
    list_with_grades = [f'{x:.2f}' for x in info]
    print(f"{every_student} -> {' '.join(list_with_grades)} (avg: {average_sum:.2f})")
