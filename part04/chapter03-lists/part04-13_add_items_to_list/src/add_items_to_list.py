items = int(input("How many items: "))
list = []
i = items + 1

while items > 0:
    item = int(input(f"Item {i - items}: "))
    list.append(item)
    items -= 1
    
print(list)