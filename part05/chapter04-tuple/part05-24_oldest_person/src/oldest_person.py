def oldest_person(people: list):
    year = people[0][1]
    name = people[0][0]
    for person in people:
        if person[1] < year:
            year = person[1]
            name = person[0]
    return name