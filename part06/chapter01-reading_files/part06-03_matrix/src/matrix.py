def read_matrix():
    matrix = []
    with open("matrix.txt") as new_file:
        for line in new_file:
            line_data = line.replace("\n", "")
            row_data = line_data.split(",")
            row = []
            for i in range(len(row_data)):
                row.append(int(row_data[i]))
            matrix.append(row)
    return matrix

def matrix_sum():
    matrix = read_matrix()
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total

def matrix_max():
    matrix = read_matrix()
    max = 0
    for row in matrix:
        for value in row:
            if value > max:
                max = value
    return max

def row_sums():
    matrix = read_matrix()
    lst = []
    for row in matrix:
        total = sum(row)
        lst.append(total)
    return lst