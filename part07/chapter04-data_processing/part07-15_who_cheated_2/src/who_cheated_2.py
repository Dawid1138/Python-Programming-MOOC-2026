import datetime

def final_points():
    nested_dct = {}
    start_dct = {}

    with open ("start_times.csv") as f1, open ("submissions.csv") as f2:

        for line in f1:
            parts = line.strip().split(";")
            start_time = datetime.datetime.strptime(parts[1], "%H:%M")
            start_dct[parts[0]] = start_time

        for line in f2:
            parts = line.strip().split(";")
            exercise = int(parts[1])
            points = int(parts[2])

            end_time = datetime.datetime.strptime(parts[3], "%H:%M")
            if parts[0] in start_dct and start_dct[parts[0]] + datetime.timedelta(hours=3) < end_time:
                continue

            if parts[0] not in nested_dct:
                nested_dct[parts[0]] = [0, 0, 0, 0, 0, 0, 0, 0]

            points_to_compare = nested_dct[parts[0]][exercise - 1]
            if points > points_to_compare:
                nested_dct[parts[0]][exercise - 1] = points

        return read_nested_dict(nested_dct)


def read_nested_dict(nested_dct):
    students_dct = {}

    for student in nested_dct:
        points = sum(nested_dct[student])
        students_dct[student] = points

    return students_dct