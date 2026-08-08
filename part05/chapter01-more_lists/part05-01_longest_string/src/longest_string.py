def longest(strings: list):
    name = ""
    for string in strings:
        if len(string) > len(name):
            name = string
    return name