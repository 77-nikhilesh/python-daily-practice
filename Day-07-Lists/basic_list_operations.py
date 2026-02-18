# Day 07 – Basic List Operations

nums = [10, 20, 30, 40, 50]

# 1. Print list
print(nums)  # [10, 20, 30, 40, 50]

# 2. Length of list
print(len(nums))  # 5

# 3. Access first and last element
print(nums[0], nums[-1])  # 10 50

# 4. Sum of elements
print(sum(nums))  # 150

# 5. Average of elements
print(sum(nums) / len(nums))  # 30.0

# 6. Maximum and minimum
print(max(nums), min(nums))  # 50 10

# 7. Reverse list using slicing
print(nums[::-1])  # [50, 40, 30, 20, 10]

# 8. Reverse list using loop
rev = []
for i in nums:
    rev.insert(0, i)
print(rev)  # [50, 40, 30, 20, 10]

# 9. Check element existence
print(30 in nums)  # True

# 10. Copy list
copy_list = nums.copy()
print(copy_list)  # [10, 20, 30, 40, 50]
