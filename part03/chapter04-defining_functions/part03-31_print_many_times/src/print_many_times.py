def print_many_times(text, times):
    amount = 1
    while amount <= times:
        print(text)
        amount += 1

if __name__ == "__main__":
    print_many_times("python", 5)