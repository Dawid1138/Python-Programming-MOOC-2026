def read_fruits():
    dict = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line_data = line.replace("\n", "")
            fruit_data = line_data.split(";")
            fruit = fruit_data[0]
            price = float(fruit_data[1])
            dict[fruit] = price
    return dict
            