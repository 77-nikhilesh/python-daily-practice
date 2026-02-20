nums = {5, 10, 15, 20, 25}

# Iteration
for n in nums:
    print(n, end=" ")
print()

# Even numbers
for n in nums:
    if n % 2 == 0:
        print("Even:", n)      # 10 20

# Count greater than 15
count = 0
for n in nums:
    if n > 15:
        count += 1
print("Count:", count)         # 2

# Sum of elements
print(sum(nums))               # 75