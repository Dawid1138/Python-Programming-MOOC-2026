def shortest(list):
    shortest_word = list[0]
    for word in list:
        if len(word) < len(shortest_word):
            shortest_word = word
    return shortest_word