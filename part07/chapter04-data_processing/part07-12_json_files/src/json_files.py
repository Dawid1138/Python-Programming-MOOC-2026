from json import load

def print_persons(filename: str):
    with open(filename) as f:
        data = load(f)
        for person in data:
            hobbies = ", ".join(person['hobbies'])
            print(f"{person['name']} {person['age']} years ({hobbies})")