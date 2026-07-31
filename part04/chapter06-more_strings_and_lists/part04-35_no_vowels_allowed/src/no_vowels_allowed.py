def no_vowels(string):
    new_string = ""
    for character in string:
        if character not in "aeiou":
            new_string += character
    return new_string