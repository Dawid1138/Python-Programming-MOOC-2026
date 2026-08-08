import string
alphabet_list = list(string.ascii_uppercase)

layers = int(input("Layers: "))
rows = layers * 2 - 1
columns = rows

for row in range(rows):
    for column in range(columns):
        row_backward = rows - row - 1
        column_backward = columns - column - 1
        lst = [row, row_backward, column, column_backward]
        smallest = min(lst)
        letter = rows - smallest - layers
        print(alphabet_list[letter], end="")
    print()