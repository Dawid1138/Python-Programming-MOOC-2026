def chessboard(size):
    row = 0

    while row < size:
        if row % 2 == 0:
            print(("10" * size)[:size])
        else:
            print(("01" * size)[:size])

        row += 1