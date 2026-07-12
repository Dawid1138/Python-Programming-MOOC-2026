def squared(word, number):
    row = 0
    index = 0
    while row < number:
        letter = 0
        while letter < number:
            print(word[index % len(word)], end="")
            index += 1
            letter += 1
        print()
        row += 1