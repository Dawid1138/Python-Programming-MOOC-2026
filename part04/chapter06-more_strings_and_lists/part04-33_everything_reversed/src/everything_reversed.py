def everything_reversed(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item[::-1])
    return new_lst[::-1]
