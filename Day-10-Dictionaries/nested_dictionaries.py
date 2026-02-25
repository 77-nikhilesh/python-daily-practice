students = {
    101: {"name": "A", "marks": 85},
    102: {"name": "B", "marks": 72},
    103: {"name": "C", "marks": 90}
}

# Print all students
for sid, info in students.items():
    print(sid, info["name"], info["marks"])

# Highest marks
top = max(students.values(), key=lambda x: x["marks"])
print(top)                             # {'name': 'C', 'marks': 90}

# Count passed students
count = 0
for s in students.values():
    if s["marks"] >= 75:
        count += 1
print("Passed:", count)                # 2