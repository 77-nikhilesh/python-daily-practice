"""
Day 10 – Real World Problems using Dictionaries
"""

# 1. Login system
users = {"admin": "1234", "user": "abcd"}
username = "admin"
password = "1234"

if users.get(username) == password:
    print("Login Successful")
else:
    print("Invalid Login")

# 2. Product billing
prices = {"Pen": 10, "Book": 50, "Bag": 500}
total = 0
for p in prices.values():
    total += p
print("Total Bill:", total)             # 560

# 3. Word frequency
sentence = "python is easy and python is powerful"
words = sentence.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)

# 4. Employee salary hike
emps = {"A": 25000, "B": 32000, "C": 20000}
for e in emps:
    if emps[e] < 30000:
        emps[e] += 3000
print(emps)

# 5. Student grades
marks = {"Ravi": 85, "Anil": 60, "Sita": 92}
for name, m in marks.items():
    if m >= 75:
        print(name, "Grade A")