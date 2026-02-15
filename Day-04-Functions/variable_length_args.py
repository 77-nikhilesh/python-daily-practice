# 1. *args addition
def add_numbers(*nums):
    total = sum(nums)
    print("Total:", total)
add_numbers(1,2,3)
# Output: Total: 6

# 2. **kwargs info
def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
user_info(name="Nikhilesh", age=21)
# Output:
# name: Nikhilesh
# age: 21

# 3. *args multiplication
def multiply_args(*nums):
    result = 1
    for n in nums:
        result *= n
    print("Product:", result)
multiply_args(2,3,4)
# Output: Product: 24

# 4. *args max number
def max_number(*nums):
    print("Max:", max(nums))
max_number(5,2,8,1)
# Output: Max: 8

# 5. **kwargs with default
def print_person(**kwargs):
    name = kwargs.get("name", "Unknown")
    age = kwargs.get("age", "N/A")
    print(f"Name: {name}, Age: {age}")
print_person()
print_person(name="Nikhilesh", age=21)
# Output: Name: Unknown, Age: N/A
# Output: Name: Nikhilesh, Age: 21
