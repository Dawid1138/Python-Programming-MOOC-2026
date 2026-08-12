def create_word_list(filename: str):
    word_list = []
    with open(filename) as f:
        for line in f:
            word_list.append(line.strip())
    return word_list


def find_words(search_term: str):
    word_list = create_word_list('words.txt')
    found_words = []

    if "." in search_term:
        for word in word_list:
            if len(word) == len(search_term):
                found = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        found = False
                        break
                if found:
                    found_words.append(word)


    elif "*" in search_term:

        for word in word_list:
            if search_term.startswith("*") and word.endswith(search_term[1:]):
                found_words.append(word)
            elif search_term.endswith("*") and word.startswith(search_term[:-1]):
                found_words.append(word)


    else:
        for word in word_list:
            if search_term == word:
                found_words.append(word)
    return found_words