limit = int(input("Limit: "))
number = 1
total = 1
calculation = "1"

while total < limit:
    number += 1
    total += number
    calculation += f" + {str(number)}"

print(f"The consecutive sum: {calculation} = {total}")