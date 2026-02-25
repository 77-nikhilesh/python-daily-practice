marks = {"Math": 80, "Sci": 70, "Eng": 90}

# Iterate keys
for k in marks:
    print(k)

# Iterate values
for v in marks.values():
    print(v)

# Iterate items
for sub, score in marks.items():
    print(sub, score)

# Find subjects above 75
for sub, score in marks.items():
    if score > 75:
        print("Above 75:", sub)

# Total & Average
total = sum(marks.values())
print("Total:", total)                 # 240
print("Average:", total / len(marks))  # 80.0