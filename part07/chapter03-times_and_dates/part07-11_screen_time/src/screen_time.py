from datetime import datetime, timedelta

filename = input("Filename: ")
date = input("Starting date: ")
time = int(input("How many days: "))
starting_date = datetime.strptime(date, "%d.%m.%Y")
end_date = starting_date + timedelta(days=time - 1)
total_minutes = 0
my_list = []

print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(time):
    current_date = starting_date + timedelta(days=i)
    minutes = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ")
    parts = minutes.split(" ")
    total_minutes += int(parts[0]) + int(parts[1]) + int(parts[2])
    my_list.append(f"{current_date.strftime('%d.%m.%Y')}: {parts[0]}/{parts[1]}/{parts[2]}")

with open (filename, "w") as f:
    f.write(f"Time period: {starting_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {total_minutes/time}\n")
    for line in my_list:
        f.write(line + "\n")