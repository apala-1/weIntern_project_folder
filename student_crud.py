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

def get_valid_int(value):
    """Forces the user to input a valid integer."""
    val = input(value)
    if(val.isdigit):
        return int(val)
    print("Please return a valid number.")

def get_non_empty(value):
    """Forces the user to input non-empty text."""
    while True:
        val = input(value).strip
        if val:
            return val
        print("This field cannot be empty.")

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