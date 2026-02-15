# 1. Add two numbers
def add(a, b):
    print("Sum:", a + b)
add(5, 7)
# Output: Sum: 12

# 2. Multiply three numbers
def multiply(a, b, c):
    print("Product:", a*b*c)
multiply(2, 3, 4)
# Output: Product: 24

# 3. Calculate area of rectangle
def rectangle_area(length, width):
    print("Area:", length*width)
rectangle_area(5, 10)
# Output: Area: 50

# 4. Convert Celsius to Fahrenheit
def c_to_f(c):
    print("Fahrenheit:", (c*9/5)+32)
c_to_f(25)
# Output: Fahrenheit: 77.0

# 5. Greet multiple times
def greet_times(name, times):
    for _ in range(times):
        print(f"Hello {name}")
greet_times("Nikhilesh", 3)
# Output: Hello Nikhilesh (3 times)
