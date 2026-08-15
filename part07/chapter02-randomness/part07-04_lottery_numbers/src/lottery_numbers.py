from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper + 1))
    lottery_numbers = sample(number_pool, amount)
    return sorted(lottery_numbers)