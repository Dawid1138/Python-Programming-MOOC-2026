def first_word(sentence):
    substring = " "
    if sentence.find(substring) == -1:
        return sentence
    else:
        return sentence[:sentence.find(substring)]

def second_word(sentence):
    substring = " "
    sentence = sentence[sentence.find(substring) + 1:]
    if sentence.find(substring) == -1:
        return sentence
    else:
        return sentence[:sentence.find(substring)]

def last_word(sentence):
    substring = " "
    while sentence.find(substring) != -1:
        sentence = sentence[sentence.find(substring) + 1:]
    return sentence