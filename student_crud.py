import json
import os

filename = "students.json"

if os.path.exists(filename):
    with open(filename, "r") as f:
        students = json.load(f)
else:
    students = []