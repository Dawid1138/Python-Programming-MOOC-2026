def main():
    while True:
        my_dictionary = read_dictionary()
        print("1 - Add word, 2 - Search, 3 - Quit")
        function = int(input("Function: "))
        if function == 1:
            finnish_word = input("The word in Finnish: ")
            english_word = input("The word in English: ")
            add_word(finnish_word, english_word)
            print("Dictionary entry added")
        elif function == 2:
            search_term = input("Search term:")
            for key, value in my_dictionary.items():
                if search_term in key or search_term in value:
                    print(f"{key} - {value}")
        else:
            print("Bye")
            break


def read_dictionary():
    dictionary = {}
    with open("dictionary.txt") as f:
        for line in f:
            parts = line.split(";")
            dictionary[parts[0]] = parts[1].strip()
    return dictionary


def add_word(finnish_word: str, english_word: str):
    with open("dictionary.txt", "a") as f:
        f.write(f"{finnish_word};{english_word}\n")


main()