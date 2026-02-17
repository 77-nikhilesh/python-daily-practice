# 1. Calculate final bill after discount and tax
price = 1200
discount = price * 0.10
tax = price * 0.05
final_price = price - discount + tax
print(final_price)
# Output: 1140.0

# 2. Swap two numbers using arithmetic operators
a, b = 5, 10
a = a + b
b = a - b
a = a - b
print(a, b)
# Output: 10 5

# 3. Check divisibility using modulus
num = 45
print(num % 5 == 0)
# Output: True

# 4. Power operator
print(2 ** 5)
# Output: 32

# 5. Floor division
print(17 // 3)
# Output: 5

# 6. Logical operators
x = 10
print(x > 5 and x < 15)
# Output: True

# 7. Membership operator
print("a" in "python")
# Output: False

# 8. Identity operator
a = [1, 2]
b = a
print(a is b)
# Output: True
