def exercise_points(amount):
    return amount // 10

def grade(points):
    limit = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= limit[i]:
            return i

def average(points):
    return sum(points) / len(points)

def main():
    points = []
    grades = [0] * 6

    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        parts = user_input.split()
        exm_points = int(parts[0])
        exercse_points = exercise_points(int(parts[1]))
        total_points = exm_points + exercse_points
        points.append(total_points)
        grd = 0 if exm_points < 10 else grade(total_points)
        grades[grd] += 1

    pass_rate = 100 * (len(points) - grades[0]) / len(points)
    print("Statistics:")
    print(f"Points average: {average(points):.1f}")
    print(f"Pass percentage: {pass_rate:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * grades[i]}")
main()