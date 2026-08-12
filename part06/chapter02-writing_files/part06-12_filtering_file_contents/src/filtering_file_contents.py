def filter_solutions():
    with open ("solutions.csv") as f1, open("correct.csv", "w") as f2, open("incorrect.csv", "w") as f3:
        for line in f1:
            if checker(line) == True:
                f2.write(line)
            else:
                f3.write(line)

def checker(line):
    parts = line.split(";")
    addition = parts[1].split("+")
    subtraction = parts[1].split("-")
    if len(addition) > len(subtraction):
        if int(addition[0]) + int(addition[1]) == int(parts[2]):
            return True
        else:
            return False
    else:
        if int(subtraction[0]) - int(subtraction[1]) == int(parts[2]):
            return True
        else:
            return False