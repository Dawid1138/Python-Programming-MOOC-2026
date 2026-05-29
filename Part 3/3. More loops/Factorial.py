while True:
    number1 = int(input("Please type in a number: "))
    if number1 > 0:
        factorial = 1
        number2 = number1
        while number2 > 1:
            factorial *= number2
            number2 -= 1
        print(f"The factorial of the number {number1} is {factorial}")
    else:
        break

print("Thanks and bye!")