class ListHelper:
    def doubles(my_list: list):
        new_list = []
        for number in my_list:
            if my_list.count(number) > 1 and number not in new_list:
                new_list.append(number)
        return len(new_list)

    def greatest_frequency(my_list: list):
        total = 0
        most_common_number = 0
        for number in my_list:
            if my_list.count(number) > total:
                total = my_list.count(number)
                most_common_number = number
        return most_common_number