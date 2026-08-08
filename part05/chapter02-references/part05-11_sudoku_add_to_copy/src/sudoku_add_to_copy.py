def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_new = []
    for row in sudoku:
       sudoku_new.append(row[:])
    sudoku_new[row_no][column_no] = number
    return sudoku_new

def print_sudoku(sudoku: list):
    for index1, row in enumerate(sudoku):
        for index2, number in enumerate(row):
            if number == 0:
                print("_", end="")
            else:
                print(number, end="")
            if index2 == 2 or index2 == 5:
                print("  ", end="")
            elif index2 == 8:
                print()
            else:
                print(" ", end="")
        if index1 == 2 or index1 == 5:
            print()