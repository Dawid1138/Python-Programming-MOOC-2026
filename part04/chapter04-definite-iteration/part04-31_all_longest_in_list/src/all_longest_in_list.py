def all_the_longest(list):
    longest_words = []
    longest_length = 0
    for word in list:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_words = [word]
        elif len(word) == longest_length:
            longest_words.append(word)
    return longest_words