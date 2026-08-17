def smallest_average(person1: dict, person2: dict, person3: dict):
    hours1 = (person1["result1"] + person1["result2"] + person1["result3"])/3
    hours2 = (person2["result1"] + person2["result2"] + person2["result3"])/3
    hours3 = (person3["result1"] + person3["result2"] + person3["result3"])/3
    hours = [hours1, hours2, hours3]
    if min(hours) == hours1:
        return person1
    elif min(hours) == hours2:
        return person2
    else:
        return person3