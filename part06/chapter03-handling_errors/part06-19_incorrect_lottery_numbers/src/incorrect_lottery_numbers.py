def filter_incorrect():
    with open("lottery_numbers.csv") as f1, open("correct_numbers.csv", "w") as f2:

        for line in f1:
            parts = line.split(";")
            number_list = parts[1].split(",")
            additional_list = []

            try:
                if parts[0][0:4] == "week" and int(parts[0][5:]) and len(number_list) == 7:
                    pass
                else:
                    raise ValueError
            except:
                continue

            try:
                for number in number_list:
                    if int(number) > 0 and int(number) < 40 and number not in additional_list:
                        additional_list.append(number)
                    else:
                        raise ValueError
            except:
                continue

            f2.write(line)