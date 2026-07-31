def line(length, text):
    if len(text) > 0:
        print(text[0] * length)
    else:
        print("*" * length)

def shape(size1, text1, size2, text2):
    i = 1
    while i <= size1:
        line(i, text1)
        i += 1
    i -= 1
    while size2 > 0:
        line(i, text2)
        size2 -= 1