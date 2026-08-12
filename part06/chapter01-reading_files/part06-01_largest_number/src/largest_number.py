def largest():
    with open("numbers.txt") as new_file:
        lst = []
        for line in new_file:
            number = line.replace("\n", "")
            lst.append(int(number))
        return max(lst)