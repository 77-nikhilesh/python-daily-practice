students = (
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90)
)

for name, marks in students:
    print(name, marks)
# Alice 85
# Bob 72
# Charlie 90

# Highest marks
highest = max(students, key=lambda x: x[1])
print(highest)  # ('Charlie', 90)
