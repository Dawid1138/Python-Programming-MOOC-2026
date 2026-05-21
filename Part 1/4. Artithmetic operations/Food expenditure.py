lunch_frequency = int(input("How many times a week do you eat at the student cafeteria?  "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_price = float(input("How much money do you spend on groceries in a week? "))
print("Average food expenditure: ")
total = lunch_frequency * lunch_price + groceries_price
print(f"Daily: {total / 7} euros")
print(f"Weekly: {total} euros")