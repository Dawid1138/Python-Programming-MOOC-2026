def main():
    text = input("Write text: ")
    wordlist = create_wordlist()
    for word in text.split():
        word_lower = word.lower()
        if word_lower in wordlist:
            print(word, end=" ")
        else:
            print(f"*{word}*", end=" ")

def create_wordlist():
    wordlist = []
    with open("wordlist.txt") as file:
        for line in file:
            wordlist.append(line.strip())
    return wordlist

main()