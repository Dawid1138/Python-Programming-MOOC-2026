class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        ppl_number = len(self.persons)
        ppl_height = sum([person.height for person in self.persons])
        print(f"There are {ppl_number} persons in the room, and their combined height is {ppl_height} cm.")
        for person in self.persons:
            print(person.name + " (" + str(person.height) + " cm)")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest = person
        return shortest

    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        shortest = self.shortest()
        self.persons.remove(shortest)
        return shortest