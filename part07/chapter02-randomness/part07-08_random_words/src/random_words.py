from random import sample

def read_words():
    with open("words.txt") as f:
        all_words = []
        for line in f:
            all_words.append(line.strip())
        return all_words


def words(n: int, beginning: str):
    all_words = read_words()
    starts_with_list = []
    for word in all_words:
        if word.startswith(beginning):
            starts_with_list.append(word)
    if len(starts_with_list) < n:
        raise ValueError
    return sample(starts_with_list, n)  