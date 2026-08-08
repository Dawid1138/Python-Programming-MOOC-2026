def histogram(word: str):
    dictionary = {}
    for letter in word:
        if letter not in dictionary:
            dictionary[letter] = 0
        dictionary[letter] += 1
    for key, value in dictionary.items():
        print(key + " " + "*"*value)