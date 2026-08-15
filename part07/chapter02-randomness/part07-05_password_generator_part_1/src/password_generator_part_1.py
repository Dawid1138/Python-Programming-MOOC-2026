from string import ascii_lowercase
from random import sample

def generate_password(length: int):
    letters = ascii_lowercase
    password_list = sample(letters, length)
    password = "".join(password_list)
    return password