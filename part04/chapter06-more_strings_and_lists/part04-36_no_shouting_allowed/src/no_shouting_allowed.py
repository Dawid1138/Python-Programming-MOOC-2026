def no_shouting(lst):
    new_lst = []
    for item in lst:
        if item.isupper() == False:
            new_lst.append(item)
    return new_lst