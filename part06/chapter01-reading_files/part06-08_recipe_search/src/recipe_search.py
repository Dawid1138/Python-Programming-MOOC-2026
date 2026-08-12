def create_dictionary(filename: str):
    recipe_dict = {}
    with open(filename) as file:

        for line in file:
            part = line.replace("\n", "")
            if part.lower() != part:
                value = part
                lst = []
            elif part == "":
                continue
            else:
                lst.append(part)
            recipe_dict[value] = lst

    return recipe_dict


def search_by_name(filename: str, word: str):
    name_list = []
    recipe_dict = create_dictionary(filename)

    for key in recipe_dict:
        if word.lower() in key.lower():
            name_list.append(key)

    return name_list


def search_by_time(filename: str, time: int):
    time_list = []
    recipe_dict = create_dictionary(filename)

    for key, value in recipe_dict.items():
        if int(value[0]) <= time:
            phrase = f"{key}, preparation time {value[0]} min"
            time_list.append(phrase)

    return time_list


def search_by_ingredient(filename: str, word: str):
    ingredients_list = []
    recipe_dict = create_dictionary(filename)

    for key, value in recipe_dict.items():  
        ingredients = value[1:]
        while True:
            for ing in ingredients:
                if word.lower() in ing.lower():
                    phrase = f"{key}, preparation time {value[0]} min"
                    ingredients_list.append(phrase)
                    break
            break
        
    return ingredients_list