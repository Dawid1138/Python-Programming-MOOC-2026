list = []
i = 1

while True:
    print(f"The list is now {list}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "d":
        list.append(i)
        i += 1
    elif operation == "r":
        list.remove(i - 1)
        i -= 1
    elif operation == "x":
        break

print("Bye!")