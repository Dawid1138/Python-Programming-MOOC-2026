def line(length, text):
    if len(text) > 0:
        print(text[0] * length)
    else:
        print("*" * length)

def square(size, character):
    i = size
    while i > 0:
        line(size, character)
        i -= 1