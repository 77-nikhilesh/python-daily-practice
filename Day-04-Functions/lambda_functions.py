# 1. Square using lambda
square = lambda x: x*x
print(square(5))
# Output: 25

# 2. Cube using lambda
cube = lambda x: x**3
print(cube(3))
# Output: 27

# 3. Add two numbers
add = lambda a,b: a+b
print(add(5,7))
# Output: 12

# 4. Even/Odd check
even_odd = lambda n: "Even" if n%2==0 else "Odd"
print(even_odd(8))
# Output: Even

# 5. Maximum of two numbers
maximum = lambda a,b: a if a>b else b
print(maximum(10,20))
# Output: 20
