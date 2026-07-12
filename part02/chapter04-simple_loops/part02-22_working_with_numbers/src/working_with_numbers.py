print("Please type in integer numbers. Type in 0 to finish.")
number_count = 0
total = 0
positive_number_count = 0
negative_number_count = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    if number > 0:
        positive_number_count += 1
    if number < 0:
        negative_number_count += 1

    number_count += 1
    total += number

print("... the program asks for numbers")
print(f"Numbers typed in {number_count}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / number_count}")
print(f"Positive numbers {positive_number_count}")
print(f"Negative numbers {negative_number_count}")