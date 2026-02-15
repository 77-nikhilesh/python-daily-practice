# 1. Factorial
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(5))
# Output: 120

# 2. Fibonacci
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))
# Output: 8

# 3. Sum of numbers
def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)
print(sum_n(5))
# Output: 15

# 4. Reverse a string
def reverse_string(s):
    if s=="":
        return ""
    return s[-1]+reverse_string(s[:-1])
print(reverse_string("Nikhilesh"))
# Output: hselkhiN

# 5. Count digits in number
def count_digits(n):
    if n==0:
        return 0
    return 1+count_digits(n//10)
print(count_digits(12345))
# Output: 5
