# 1. Add two numbers
def add(a, b):
    return a + b
print(add(5, 7))
# Output: 12

# 2. Check even or odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(even_odd(9))
# Output: Odd

# 3. Factorial
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f
print(factorial(5))
# Output: 120

# 4. Maximum of two numbers
def maximum(a, b):
    return a if a > b else b
print(maximum(10, 20))
# Output: 20

# 5. Palindrome number
def is_palindrome(n):
    return str(n) == str(n)[::-1]
print(is_palindrome(121))
# Output: True

# 6. Count vowels
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")
print(count_vowels("Python"))
# Output: 1

# 7. Lambda square
square = lambda x: x * x
print(square(6))
# Output: 36
