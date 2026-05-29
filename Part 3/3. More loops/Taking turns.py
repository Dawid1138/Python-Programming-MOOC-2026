number = int(input("Please type in a number: "))
index = 0

while index < (number - 1)/2:
    print(index + 1)
    print(number - index)
    index += 1

if number % 2 == 1:
    middle = int((number + 1)/2)
    print(middle)