text = input("Please type in a string: ")
number = len(text) - 1

while number >= 0:
    print(text[number:])
    number -= 1