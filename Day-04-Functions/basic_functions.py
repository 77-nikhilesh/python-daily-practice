# 1. Simple greeting function
def greet():
    print("Hello, welcome to Python functions!")
greet()
# Output: Hello, welcome to Python functions!

# 2. Separator line
def separator():
    print("-" * 20)
separator()
# Output: --------------------

# 3. Print squares from 1 to 5
def print_squares():
    for i in range(1, 6):
        print(i*i, end=" ")
    print()
print_squares()
# Output: 1 4 9 16 25

# 4. Function to say good morning
def good_morning(name):
    print(f"Good morning, {name}!")
good_morning("Nikhilesh")
# Output: Good morning, Nikhilesh!

# 5. Function to return nothing (demonstrates pass)
def do_nothing():
    pass
do_nothing()
# Output: (None)
