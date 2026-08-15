import datetime

def cheaters():
    cheater_lst = []
    start_dct = {}

    with open ("start_times.csv") as f1, open ("submissions.csv") as f2:

        for line in f1:
            parts = line.strip().split(";")
            start_time = datetime.datetime.strptime(parts[1], "%H:%M")
            start_dct[parts[0]] = start_time

        for line in f2:
            parts = line.strip().split(";")
            end_time = datetime.datetime.strptime(parts[3], "%H:%M")

            if parts[0] in cheater_lst:
                continue

            if parts[0] in start_dct and start_dct[parts[0]] + datetime.timedelta(hours=3) < end_time:
                cheater_lst.append(parts[0])

    return cheater_lst