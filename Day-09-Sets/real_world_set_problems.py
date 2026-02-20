"""
Day 09 – Real World Problems using Sets
"""

# 1. Remove duplicate student IDs
ids = [101, 102, 101, 103, 102]
unique_ids = set(ids)
print(unique_ids)              # {101, 102, 103}

# 2. Attendance comparison
day1 = {"A", "B", "C", "D"}
day2 = {"C", "D", "E"}

print("Both Days:", day1 & day2)    # {'C', 'D'}
print("Only Day1:", day1 - day2)    # {'A', 'B'}

# 3. Subjects chosen by students
math = {"Ravi", "Anil", "Sita"}
science = {"Sita", "Anil", "John"}

print("Both Subjects:", math & science)  # {'Sita', 'Anil'}

# 4. Website unique visitors
visitors = ["IP1", "IP2", "IP1", "IP3"]
print(len(set(visitors)))         # 3

# 5. Available vs Sold Products
available = {"Laptop", "Mouse", "Keyboard"}
sold = {"Mouse"}

print("Remaining:", available - sold)  # {'Laptop', 'Keyboard'}