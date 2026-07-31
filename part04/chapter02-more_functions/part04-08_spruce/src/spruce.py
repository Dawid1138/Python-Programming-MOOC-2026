def spruce(number):
    row_length = number * 2 - 1
    i = 1
    print("a spruce!")
    while i <= row_length:
        print(" " * ((row_length - i) // 2) + "*" * i)
        i += 2
    print(" " * ((row_length - 1) // 2) + "*")

if __name__ == "__main__":
    spruce(5)