# 1. break example
for i in range(1, 6):
    if i == 4:
        break
    print(i, end=" ")
# Output: 1 2 3

print()

# 2. continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
# Output: 1 2 4 5

print()

# 3. pass example
for i in range(1, 4):
    if i == 2:
        pass
    print(i)
# Output:
# 1
# 2
# 3
