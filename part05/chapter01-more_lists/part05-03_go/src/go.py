def who_won(game_board: list):
    one = 0
    two = 0
    for row in game_board:
        for item in row:
            if item == 1:
                one += 1
            elif item == 2:
                two += 1
    if one > two:
        return 1
    elif two > one:
        return 2
    else:
        return 0