# 1. Default argument greeting
def greet_user(name="User"):
    print(f"Hello {name}")
greet_user()
greet_user("Nikhilesh")
# Output: Hello User
# Output: Hello Nikhilesh

# 2. Keyword arguments demo
def user_details(name, age):
    print(f"Name: {name}, Age: {age}")
user_details(age=21, name="Nikhilesh")
# Output: Name: Nikhilesh, Age: 21

# 3. Default argument multiplication
def multiply(a, b=2):
    print("Product:", a*b)
multiply(5)
multiply(5, 3)
# Output: Product: 10
# Output: Product: 15

# 4. Keyword args with printing
def print_info(name, city="Unknown"):
    print(f"{name} lives in {city}")
print_info("Nikhilesh")
print_info("Nikhilesh", "Bangalore")
# Output: Nikhilesh lives in Unknown
# Output: Nikhilesh lives in Bangalore

# 5. Default argument sum
def add_numbers(a, b=0, c=0):
    print("Sum:", a+b+c)
add_numbers(5)
add_numbers(5, 3)
add_numbers(5, 3, 2)
# Output: Sum: 5
# Output: Sum: 8
# Output: Sum: 10
