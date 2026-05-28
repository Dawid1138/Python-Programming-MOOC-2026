text = input("Please type in a string: ")
number = 1

while number <= len(text):
    print(text[:number])
    number += 1