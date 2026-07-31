def line(length, text):
    if len(text) > 0:
        print(text[0] * length)
    else:
        print("*" * length)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1