import json
import math
import urllib.request

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    data = json.load(urllib.request.urlopen(url))
    
    active_courses = []
    for course in data:
        if course["enabled"]:
            active_courses.append((
                course["fullName"], 
                course["name"], 
                course["year"], 
                sum(course["exercises"])
            ))
    return active_courses

def retrieve_course(course_name: str):
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    data = json.load(urllib.request.urlopen(url))

    course_dict = {}
    course_dict["weeks"] = len(data)

    students = 0
    hours = 0
    exercises = 0

    for week in data.values():
        if week["students"] > students:
            students = week["students"]
        hours += week["hour_total"]
        exercises += week["exercise_total"]

    course_dict["students"] = students
    course_dict["hours"] = hours
    course_dict["hours_average"] = math.floor(hours / students)
    course_dict["exercises"] = exercises
    course_dict["exercises_average"] = math.floor(exercises / students)

    return course_dict

if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course("docker2019"))