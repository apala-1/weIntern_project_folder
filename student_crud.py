import json
import os

filename = "students.json"

if os.path.exists(filename):
    with open(filename, "r") as f:
        students = json.load(f)
else:
    students = []

def save_data():
    """Saves the students list to JSON file."""
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)

def add_student():
    print("Add student here: ")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "grade": grade,
    }

    students.append(student)
    save_data()
    print("The student is added.")