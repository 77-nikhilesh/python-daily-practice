# 1. Count digits in a number
num = 4567
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)
# Output: Digits: 4

# 2. Check if number is prime
n = 7
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")
# Output: Prime

# 3. Factorial using loop
fact = 1
num = 5
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)
# Output: Factorial: 120
