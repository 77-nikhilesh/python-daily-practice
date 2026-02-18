# Day 07 – List Traversal & Conditions

nums = [12, -7, 5, -3, 10, 0, 8]

# 1. Count positive and negative numbers
pos = neg = 0
for n in nums:
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
print(pos, neg)  # 4 2

# 2. Count even and odd numbers
even = odd = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print(even, odd)  # 4 3

# 3. Find largest element manually
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print(largest)  # 12

# 4. Find smallest element manually
smallest = nums[0]
for n in nums:
    if n < smallest:
        smallest = n
print(smallest)  # -7

# 5. Count zeros
count_zero = 0
for n in nums:
    if n == 0:
        count_zero += 1
print(count_zero)  # 1

# 6. Index of an element
print(nums.index(10))  # 4

# 7. Square of each element
squares = []
for n in nums:
    squares.append(n * n)
print(squares)  # [144, 49, 25, 9, 100, 0, 64]
