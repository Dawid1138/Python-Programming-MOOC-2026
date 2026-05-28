text = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index1 = text.find(substring)
if index1 == -1:
    print("The substring does not occur twice in the string.")
else:
    text = text[index1 + len(substring):]
    index2 = text.find(substring)
    if index2 == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {index1 + index2 + len(substring)}.")