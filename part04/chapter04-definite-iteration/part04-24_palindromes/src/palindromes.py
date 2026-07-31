def palindromes(str1):
    str2 = str1[::-1]
    return str1 == str2

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word) == False:
        print("that wasn't a palindrome")
    else:
        print(f"{word} is a palindrome!")
        break