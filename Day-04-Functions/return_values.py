# 1. Square of a number
def square(n):
    return n*n
print("Square of 5:", square(5))
# Output: Square of 5: 25

# 2. Cube of a number
def cube(n):
    return n**3
print("Cube of 3:", cube(3))
# Output: Cube of 3: 27

# 3. Check even or odd
def even_odd(n):
    return "Even" if n%2==0 else "Odd"
print(even_odd(8))
# Output: Even

# 4. Maximum of two numbers
def maximum(a, b):
    return a if a>b else b
print("Max:", maximum(10, 20))
# Output: Max: 20

# 5. Factorial using return
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print("Factorial of 5:", factorial(5))
# Output: Factorial of 5: 120
