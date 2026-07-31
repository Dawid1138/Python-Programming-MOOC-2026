def range_of_list(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)