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
    print("Add student here: \n")
    name = input("Name: ")
    age = get_valid_int("Age: ")
    grade = input("Grade: ")

    student = {
        "id": len(students) + 1,
        "name": name,
        "age": age,
        "grade": grade,
    }

    students.append(student)
    save_data()
    print("The student is added.\n")

def update_student():
    print("Update student here: \n")
    student_id = get_valid_int("Enter ID: ")

    for s in students:
        if s["id"] == student_id:
            new_name = input(f"Name [{s['name']}]: ").strip()
            if new_name:
                s['name'] = new_name

            new_age = input(f"Age [{s['age']}]: ").strip()
            if new_age:
                s['age'] = new_age

            new_grade = input(f"Grade: [{s['grade']}]: ").strip()
            if new_grade:
                s['grade'] = new_grade

            save_data()
            print("Update Sucessful.\n")
            return

        print("Student not found.\n")

def delete_student():
    print("Delete student here: \n")
    student_id = input("Enter Student ID: ")

    global students
    previous_length = len(students)
    updated_students = []
    for s in students:
        if s['id'] == int(student_id):
            found = True
        else:
            updated_students.append(s)

    if len(updated_students) < previous_length:
        students = updated_students
        save_data()
        print("Deletion sucessful.\n")
    else:
        print("Student not found.\n")   

def view_students():
    print("View Students here: \n")
    print(f"{'ID':<5}{'Name':<20}{'Age':<5}{'Grade':<5}")
    print("-" * 35)

    for s in students:
        print(f"{s['id']:<5}{s['name']:<20}{s['age']:<5}{s['grade']:<5}")
       
    print()