word = input("Word: ")
print("*"*30)
if len(word) % 2 == 1:
    print("*" + " "*((27 - len(word))//2) + word + " "*((29 - len(word))//2) + "*")
else:
    print("*" + " " * ((28 - len(word)) // 2) + word + " " * ((28 - len(word)) // 2) + "*")
print("*"*30)