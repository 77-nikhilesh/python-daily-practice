"""
Problem: Check whether required technologies are present in a candidate's skill set.

"""

skills = ["Python", "Git", "SQL", "Docker"]
required_skill = "Python"

print("Skill present:", required_skill in skills)
print("Skill not present:", "Java" not in skills)

# Output:
# Skill present: True
# Skill not present: True
