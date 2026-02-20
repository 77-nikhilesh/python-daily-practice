# Set creation
s = {10, 20, 30, 40}
print(s)                       # {10, 20, 30, 40}

# Duplicate removal
nums = {1, 2, 2, 3, 3, 4}
print(nums)                    # {1, 2, 3, 4}

# Empty set
empty = set()
print(type(empty))             # <class 'set'>

# Membership
print(20 in s)                 # True
print(50 in s)                 # False

# Length
print(len(s))                  # 4

# Convert list to set
lst = [1, 2, 2, 3, 4]
print(set(lst))                # {1, 2, 3, 4}