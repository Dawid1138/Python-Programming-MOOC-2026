def line(length, text):
    if len(text) > 0:
        print(text[0] * length)
    else:
        print("*" * length)