def column_correct(sudoku: list, column_no: int):
    new_list = []
    for row in sudoku:
        new_list.append(row[column_no])
    for i in range(1, 10):
        if new_list.count(i) > 1:
            return False
    return True