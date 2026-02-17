# 1. Check pass or fail
marks = 38
if marks >= 35:
    print("Pass")
else:
    print("Fail")
# Output: Pass

# 2. Even or odd
num = 17
print("Even" if num % 2 == 0 else "Odd")
# Output: Odd

# 3. Greatest of three numbers
a, b, c = 10, 25, 15
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)
# Output: 25

# 4. Leap year check
year = 2024
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
# Output: Leap Year

# 5. Voting eligibility
age = 20
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
# Output: Eligible

# 6. Grade calculation
score = 82
if score >= 90:
    print("A")
elif score >= 75:
    print("B")
else:
    print("C")
# Output: B

# 7. Login validation
username = "admin"
password = "1234"
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")
# Output: Login Successful
