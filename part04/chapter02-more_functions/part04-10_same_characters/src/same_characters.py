def same_chars(word, index1, index2):
    if len(word) > index1 and len(word) > index2:
        return word[index1] == word[index2]
    return False