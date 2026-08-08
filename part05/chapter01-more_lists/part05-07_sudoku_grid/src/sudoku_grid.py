def  row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for i in range(1, 10):
        if row.count(i) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    new_list = []
    for row in sudoku:
        new_list.append(row[column_no])
    for i in range(1, 10):
        if new_list.count(i) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    new_list = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            new_list.append(sudoku[i][j])
    for i in range(1, 10):
        if new_list.count(i) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i):
            return False

    for i in range(9):
        if not column_correct(sudoku, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(sudoku, i, j):
                return False

    return True