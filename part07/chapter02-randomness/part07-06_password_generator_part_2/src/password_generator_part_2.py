from string import ascii_lowercase, digits
from random import choice

def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    letters_import = ascii_lowercase
    numbers_import = digits
    characters_import = "!?=+-()#"

    my_string = letters_import
    if numbers:
        my_string += numbers_import
    if special_characters:
        my_string += characters_import

    while True:
        password = ""
        for i in range(length):
            password += choice(my_string)
        if numbers:
            if not check_numbers(password):
                continue
        if special_characters:
            if not check_special_characters(password):
                continue
        return password


def check_numbers(password):
    for char in password:
        if char in digits:
            return True
    return False

def check_special_characters(password):
    for char in password:
        if char in "!?=+-()#":
            return True
    return False