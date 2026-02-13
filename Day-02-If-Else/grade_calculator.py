"""
Problem: Calculate grade based on percentage.
"""

percentage = 82

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

# Output:
# Grade: B
