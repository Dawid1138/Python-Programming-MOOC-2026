from difflib import get_close_matches

def main():
    text = input("Write text: ")
    wordlist = create_wordlist()
    wrong_wordlist = []

    for word in text.split():
        word_lower = word.lower()
        if word_lower in wordlist:
            print(word, end=" ")
        else:
            print(f"*{word}*", end=" ")
            wrong_wordlist.append(word)

    if len(wrong_wordlist) > 0:
        print("\nsuggestions:", end = "")

        for word in wrong_wordlist:
            print(f"\n{word}:", end = "")
            suggestions = get_close_matches(word, wordlist)

            for i in range(len(suggestions)):
                if i != len(suggestions) - 1:
                    print(f" {suggestions[i]},", end = "")
                else:
                    print(f" {suggestions[i]}", end = "")

def create_wordlist():
    wordlist = []
    with open("wordlist.txt") as file:

        for line in file:
            wordlist.append(line.strip())

    return wordlist

main()