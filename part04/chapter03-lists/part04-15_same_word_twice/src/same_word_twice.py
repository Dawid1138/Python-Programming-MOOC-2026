list = []

while True:
    word = input("Type a word: ")
    if word in list:
        print(f"You typed in {len(list)} different words")
        break
    else:
        list.append(word)