# 1. Print numbers from 5 to 1
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
# Output: 5 4 3 2 1

print()

# 2. Sum of first 5 natural numbers
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Sum:", total)
# Output: Sum: 15

# 3. Reverse a number
num = 123
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)
# Output: Reversed: 321
