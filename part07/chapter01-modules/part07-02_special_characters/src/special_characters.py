from string import *

def separate_characters(my_string: str):
    letters = ""
    punctuations = ""
    strange_letters = ""
    for letter in my_string:
        if letter in ascii_letters:
            letters += letter
        elif letter in punctuation:
            punctuations += letter
        else:
            strange_letters += letter
    return letters, punctuations, strange_letters