def add_student(dictionary: dict, student: str):
    if student not in dictionary:
        dictionary[student] = []


def print_student(dictionary: dict, student: str):
    if student not in dictionary:
        print(f"{student}: no such person in the database")

    else:

        if len(dictionary[student]) == 0:
            print(f"{student}:")
            print(" no completed courses")

        else:
            all_grades = len(dictionary[student])
            sum_grades = 0
            print(f"{student}:")
            print(f" {all_grades} completed courses:")
            for course, grade in dictionary[student]:
                print(f"  {course} {grade}")
                sum_grades += grade
            print(f" average grade {sum_grades / all_grades}")


def add_course(dictionary: dict, student: str, course: tuple):
    course_name, grade = course
    if grade == 0:
        return
    
    if student not in dictionary:
        add_student(dictionary, student)

    for i in range(len(dictionary[student])):
        if dictionary[student][i][0] == course_name:
            if dictionary[student][i][1] < grade:
                dictionary[student][i] = (course_name, grade)
            return
            
    dictionary[student].append((course_name, grade))


def summary(dictionary: dict):
    most_courses = 0
    best_average_grade = 0
    hardworker = ""
    best_student = ""
    for student in dictionary:
        grade_sum = 0

        if len(dictionary[student]) > most_courses:
            most_courses = len(dictionary[student])
            hardworker = student
        for i in range(len(dictionary[student])):
            grade_sum += dictionary[student][i][1]

        if len(dictionary[student]) > 0:
            average_grade = grade_sum / len(dictionary[student])
            if average_grade > best_average_grade:
                best_average_grade = average_grade
                best_student = student

    print(f"students {len(dictionary)}")
    print(f"most courses completed {most_courses} {hardworker}")
    print(f"best average grade {best_average_grade} {best_student}")