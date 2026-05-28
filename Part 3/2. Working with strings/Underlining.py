while True:
    text = input("Please type in a string: ")
    if text != "":
        print(text)
        print("_" * len(text))
    else:
        break