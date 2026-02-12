"""
Problem: Check eligibility for a software job using logical operators.

"""

age = 22
degree_completed = True
has_projects = False

print("Eligible using AND:", age >= 21 and degree_completed)
print("Eligible using OR:", has_projects or degree_completed)
print("NOT has projects:", not has_projects)

# Output:
# Eligible using AND: True
# Eligible using OR: True
# NOT has projects: True
