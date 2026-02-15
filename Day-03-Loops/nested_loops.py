# 1. Multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end=" ")
    print()

# Output:
# 1 2 3
# 2 4 6
# 3 6 9

# 2. Print coordinate pairs
for i in range(1, 3):
    for j in range(1, 3):
        print(f"({i},{j})", end=" ")
    print()
# Output:
# (1,1) (1,2)
# (2,1) (2,2)
