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

