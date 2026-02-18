# Day 07 – List Methods Practice

nums = [3, 1, 4, 1, 5]

# 1. append()
nums.append(9)
print(nums)  # [3, 1, 4, 1, 5, 9]

# 2. extend()
nums.extend([2, 6])
print(nums)  # [3, 1, 4, 1, 5, 9, 2, 6]

# 3. insert()
nums.insert(2, 10)
print(nums)  # [3, 1, 10, 4, 1, 5, 9, 2, 6]

# 4. remove()
nums.remove(1)
print(nums)  # removes first occurrence of 1

# 5. pop()
nums.pop()
print(nums)

# 6. count()
print(nums.count(1))  # frequency of 1

# 7. index()
print(nums.index(5))  # index of 5

# 8. sort()
nums.sort()
print(nums)

# 9. reverse()
nums.reverse()
print(nums)

# 10. clear()
temp = nums.copy()
temp.clear()
print(temp)  # []
