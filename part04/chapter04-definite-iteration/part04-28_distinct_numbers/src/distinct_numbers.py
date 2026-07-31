def distinct_numbers(list):
    distinct = []
    for number in list:
        if number not in distinct:
            distinct.append(number)
    return sorted(distinct)