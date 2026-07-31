def longest_series_of_neighbours(lst):
    new_lst = [lst[0]]
    length = 1
    number = lst[0]

    for item in lst[1:]:
        if item == number + 1 or item == number - 1:
            new_lst.append(item)
        else:
            if len(new_lst) > length:
                length = len(new_lst)
            new_lst = [item]
        number = item

    if len(new_lst) > length:
        length = len(new_lst)

    return length

if __name__ == "__main__":
    print(longest_series_of_neigbours([1, 2, 3, 5, 6, 9, 10]))