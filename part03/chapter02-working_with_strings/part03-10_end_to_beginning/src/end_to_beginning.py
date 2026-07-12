string = input("Please type in a string: ")
number = 0

while number < len(string):
    number += 1
    print(string[len(string) - number])