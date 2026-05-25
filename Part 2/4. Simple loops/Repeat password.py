password1 = input("Password: ")

while True:
    password2 = input("Repeat Password: ")
    if password1 == password2:
        break
    if password1 != password2:
        print("They do not match!")

print("User account created!")