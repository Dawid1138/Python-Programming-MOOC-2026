editor_lower = ""
while editor_lower != "visual studio code":
    editor = input("Editor: ")
    editor_lower = editor.lower()
    if editor_lower == "word" or editor_lower == "notepad":
        print("awful")
    elif editor_lower != "visual studio code":
        print("not good")
print("an excellent choice!")    