number = int(input("Please type in a number: "))
operand1 = 1
operand2 = 1

while operand1 - 1 != number and operand2 != number:
    while operand2 <= number:
        print(f"{operand1} x {operand2} = {operand2 * operand1}")
        operand2 += 1
    operand1 += 1
    operand2 = 1