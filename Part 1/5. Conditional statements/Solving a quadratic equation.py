from math import sqrt
print("ax² + bx + c = 0")
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / (2*a)
    x2 = (-b - sqrt(discriminant)) / (2*a)
    print(f"The roots are {x1} and {x2}")
if discriminant == 0:
    x = -b/(2*a)
    print(f"The root is {x}")
if discriminant < 0:
    print("There is no real root")