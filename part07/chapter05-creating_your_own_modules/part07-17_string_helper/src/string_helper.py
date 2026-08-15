def change_case(orig_string: str):
    new_str = ""
    for char in orig_string:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str


def split_in_half(orig_string: str):
    if len(orig_string) % 2 != 0:
        return orig_string[0:(len(orig_string) // 2)], orig_string[len(orig_string) // 2:]
    else:
        return orig_string[0:(len(orig_string) // 2)], orig_string[len(orig_string) // 2:]


def remove_special_characters(orig_string: str):
    new_str = ""
    for char in orig_string:
        if char.isalnum() or char == " ":
            new_str += char
    return new_str