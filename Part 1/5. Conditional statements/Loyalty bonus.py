points = int(input("How many points are on your card? "))
if points < 100:
    points_received = 1.1 * points
    print("Your bonus is 10 %")

if points >= 100:
    points_received = 1.15 * points
    print("Your bonus is 15 %")

print("You now have", points_received, "points")