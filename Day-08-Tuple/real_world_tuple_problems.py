"""
Day 08 Real World Problems using Tuples.
Tuples are used for fixed and read-only data.
"""

# 1. Student Record System
student = (101, "Nikhilesh", "CSE", 8.5)

print("ID:", student[0])        # 101
print("Name:", student[1])      # Nikhilesh
print("Branch:", student[2])    # CSE
print("CGPA:", student[3])      # 8.5


# 2. Product Price List (Immutable)
products = (
    ("Laptop", 55000),
    ("Mouse", 500),
    ("Keyboard", 1200)
)

for p in products:
    print(p[0], p[1])
# Laptop 55000
# Mouse 500
# Keyboard 1200


# 3. Coordinate Points
point = (4, 7)
x, y = point

print("X:", x)   # 4
print("Y:", y)   # 7


# 4. Days and Attendance
attendance = ("P", "A", "P", "P", "P", "A")

print("Present Days:", attendance.count("P"))  # 4
print("Absent Days:", attendance.count("A"))   # 2


# 5. Employee Salary Slip
employee = ("E102", "Ravi", 32000)

eid, name, salary = employee
print(name, "Salary:", salary)  # Ravi Salary: 32000
