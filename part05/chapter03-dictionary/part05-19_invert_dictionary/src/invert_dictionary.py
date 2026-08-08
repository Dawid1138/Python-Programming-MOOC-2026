def invert(dictionary: dict):
    copy = {}
    for key in dictionary:
        copy[key] = dictionary[key]
    dictionary.clear()
    for key in copy:
        dictionary[copy[key]] = key