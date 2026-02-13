"""
Problem: Check login access based on username and password.
"""

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")

# Output:
# Login successful
