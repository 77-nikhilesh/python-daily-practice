emp = {"id": 201, "name": "Ravi", "salary": 25000}

# Access values
print(emp["name"])                     # Ravi
print(emp.get("salary"))               # 25000

# Update value
emp["salary"] = 28000
print(emp["salary"])                   # 28000

# Add new key
emp["dept"] = "IT"
print(emp)

# Remove key
emp.pop("dept")
print(emp)

# Clear dictionary
temp = {"x": 1}
temp.clear()
print(temp)                            # {}