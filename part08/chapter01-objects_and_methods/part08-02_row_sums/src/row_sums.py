def row_sums(my_matrix: list):
    matrix = []
    for row in my_matrix:
        row.append(sum(row))