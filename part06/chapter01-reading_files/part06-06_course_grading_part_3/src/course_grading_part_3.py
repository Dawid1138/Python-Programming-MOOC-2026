def main():
    student_data = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")

    names_dict = read_student_info(student_data)
    exercises_dict = read_exercise_data(exercise_data)
    exam_points_dict = read_exam_data(exam_data)
    print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")

    for student_id, name in names_dict.items():
        total_points = 0

        if student_id in exercises_dict:
            exercises_number = exercises_dict[student_id]
            exercises_points = calculate_exercises_points(exercises_dict[student_id])
            total_points += exercises_points
        else:
            exercises_points = 0
            exercises_number = 0

        if student_id in exam_points_dict:
            exam_points = exam_points_dict[student_id]
            total_points += exam_points
        else:
            exam_points = 0

        grade_value = grade(total_points)

        print(f"{name:<30}{exercises_number:<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade_value:<10}")


def read_student_info(student_data):
    names = {}
    with open(student_data) as file:

        for line in file:
            parts = line.strip().split(";")
            if parts[0] == "id":
                continue
            student_id = parts[0]
            name = parts[1] + " " + parts[2]
            names[student_id] = name

    return names


def read_exercise_data(exercise_data):
    exercises_number = {}
    with open(exercise_data) as file:

        for line in file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            student_id = parts[0]
            exercises_list = parts[1:]
            total_exercises = 0
            for number in exercises_list:
                total_exercises += int(number)
            exercises_number[student_id] = total_exercises

    return exercises_number


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
            for points in exam_points_list:
                total_exam_points += int(points)
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