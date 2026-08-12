while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(f"{entry}\n")
        print("Diary saved")
    else:
        with open("diary.txt") as file:
            print("Entries:")
            print(file.read())