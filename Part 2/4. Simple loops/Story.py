story = ""
previous_word = ""

while True:
    word = input("Please type in a word: ")
    if word == "end" or word == previous_word:
        break
    if word != "end":
        story += word + " "
        previous_word = word

print(story)