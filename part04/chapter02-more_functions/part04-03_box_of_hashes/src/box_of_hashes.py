def line(length, text):
    if len(text) > 0:
        print(text[0] * length)
    else:
        print("*" * length)

def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1