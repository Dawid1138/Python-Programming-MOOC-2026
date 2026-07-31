def sum_of_positives(list):
    total = 0
    for i in range(len(list)):
        if list[i] > 0:
            total += list[i]
    return total