def main():
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

    names = read_student_info(student_info)
    points = read_exercise_data(exercise_data)

    for student_id, name in names.items():
        if student_id in points:
            print(f"{name} {points[student_id]}")
        else:
            print(f"{name} 0")


def read_student_info(student_info):
    names = {}
    with open(student_info) as file:

        for line in file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            student_id = parts[0]
            name = parts[1] + " " + parts[2].strip()
            names[student_id] = name

    return names


def read_exercise_data(exercise_data):
    exercises_done = {}
    with open(exercise_data) as file:

        for line in file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            student_id = parts[0]
            exercises_list = parts[1:]
            total_exercises = 0
            for amount in exercises_list:
                total_exercises += int(amount)
            exercises_done[student_id] = total_exercises

    return exercises_done


main()