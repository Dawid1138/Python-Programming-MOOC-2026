sentence = input("Please type in a sentence: ")
substring = " "
index = 0

while index != -1:
    print(sentence[:1])
    index = sentence.find(substring)
    sentence = sentence[index + 1:]