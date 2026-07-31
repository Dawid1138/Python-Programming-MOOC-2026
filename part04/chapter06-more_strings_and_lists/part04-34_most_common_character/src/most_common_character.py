def most_common_character(string):
    character_count = 0
    for character in string:
        if string.count(character) > character_count:
            character_count = string.count(character)
            most_common = character
    return most_common