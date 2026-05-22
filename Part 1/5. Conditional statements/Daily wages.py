hourly_wage = float(input("Hourly wage:  "))
hours = int(input("Hours worked: "))
day = input("Day of the week: ")
daily_wage = hourly_wage * hours
if day != "Sunday":
    print(f"Daily wages: {daily_wage} euros")
if day == "Sunday":
    print(f"Daily wages: {daily_wage * 2} euros")
