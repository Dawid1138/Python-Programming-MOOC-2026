def read_input(text: str, lower_limit: int, upper_limit: int):

    while True:
        try:
            number = int(input(text))
            if number >= lower_limit and number <= upper_limit:
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {lower_limit} and {upper_limit}")