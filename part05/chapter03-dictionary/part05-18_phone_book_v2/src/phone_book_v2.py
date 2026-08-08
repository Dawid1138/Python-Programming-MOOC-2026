phone_book = {}

while True:
    answer = int(input("command (1 search, 2 add, 3 quit): "))

    if answer == 2:
        name = input("name: ")
        number = input("number: ")
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print("ok!")

    elif answer == 1:
        name = input("name: ")
        if name in phone_book:
            for num in phone_book[name]:
                print(num)
        else:
            print("no number")

    elif answer == 3:
        print("quitting...")
        break