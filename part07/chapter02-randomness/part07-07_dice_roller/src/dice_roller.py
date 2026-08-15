from random import choice

def roll(die: str):
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return choice([1, 4, 4, 4, 4, 4])


def play(die1: str, die2: str, times: int):
    wins = 0
    losses = 0
    draws = 0
    for i in range(times):
        result = roll(die1) - roll(die2)
        if result > 0:
            wins += 1
        elif result < 0:
            losses += 1
        else:
            draws += 1
    return (wins, losses, draws)