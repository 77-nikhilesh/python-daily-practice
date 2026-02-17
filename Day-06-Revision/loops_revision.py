# 1. Print numbers 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()

# Output: 1 2 3 4 5 6 7 8 9 10

# 2. Sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print(total)
# Output: 55

# 3. Reverse a number
num = 123
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)
# Output: 321

# 4. Count digits
num = 56789
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)
# Output: 5

# 5. Prime number check
n = 11
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")
# Output: Prime

# 6. Factorial
fact = 1
for i in range(1, 6):
    fact *= i
print(fact)
# Output: 120

# 7. Star pattern
for i in range(1, 4):
    print("*" * i)

# Output:
# *
# **
# ***

# 8. Loop with else
for i in range(3):
    print(i)
else:
    print("Done")
# Output:
# 0
# 1
# 2
# Done
