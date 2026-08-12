def main():
    student_data = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")

    names = read_student_info(student_data)
    exercises_points = read_exercise_data(exercise_data)
    exam_points = read_exam_data(exam_data)

    for student_id, name in names.items():
        total_points = 0

        if student_id in exercises_points:
            total_points += calculate_exercises_points(
                exercises_points[student_id]
            )

        if student_id in exam_points:
            total_points += exam_points[student_id]

        print(f"{name} {grade(total_points)}")


def read_student_info(student_data):
    names = {}

    with open(student_data) as file:
        for line in file:
            parts = line.split(";")

            if parts[0] == "id":
                continue

            student_id = parts[0]
            name = parts[1] + " " + parts[2].strip()
            names[student_id] = name

    return names


def read_exercise_data(exercise_data):
    exercises_points = {}

    with open(exercise_data) as file:
        for line in file:
            parts = line.split(";")

            if parts[0] == "id":
                continue

            student_id = parts[0]
            exercises_points_list = parts[1:]
            total_exercises_points = 0

            for amount in exercises_points_list:
                total_exercises_points += int(amount)

            exercises_points[student_id] = total_exercises_points

    return exercises_points


def read_exam_data(exam_data):
    exam_points = {}

    with open(exam_data) as file:
        for line in file:
            parts = line.split(";")

            if parts[0] == "id":
                continue

            student_id = parts[0]
            exam_points_list = parts[1:]
            total_exam_points = 0

            for amount in exam_points_list:
                total_exam_points += int(amount)

            exam_points[student_id] = total_exam_points

    return exam_points


def grade(total_points: int):
    lst = [14, 17, 20, 23, 27]

    for i in range(len(lst)):
        if total_points <= lst[i]:
            return i

    return 5


def calculate_exercises_points(exercises_points: int):
    points = 0

    for i in range(4, 41, 4):
        if exercises_points < i:
            return points

        points += 1

    return points


main()