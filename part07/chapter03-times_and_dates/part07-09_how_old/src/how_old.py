from datetime import datetime

def main():
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    date_born = datetime(year, month, day)
    date_eve = datetime(2000, 1, 1)
    difference = date_eve - date_born
    correct_days = difference.days - 1
    if correct_days < 0:
        print("You weren't born yet on the eve of the new millennium.")
    else:
        print(f"You were {correct_days} days old on the eve of the new millennium.")

main()