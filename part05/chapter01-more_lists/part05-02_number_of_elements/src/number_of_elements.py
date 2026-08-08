def count_matching_elements(my_matrix: list, element: int):
    total = 0
    for row in my_matrix:
        for item in row:
            if item == element:
                total += 1
    return total