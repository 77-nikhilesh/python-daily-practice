matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print matrix
for row in matrix:
    print(row)

# 2. Sum of all elements
total = 0
for row in matrix:
    for val in row:
        total += val
print(total)  # 45

# 3. Row-wise sum
for row in matrix:
    print(sum(row))  # 6, 15, 24

# 4. Find maximum element
max_val = matrix[0][0]
for row in matrix:
    for val in row:
        if val > max_val:
            max_val = val
print(max_val)  # 9

# 5. Flatten list
flat = []
for row in matrix:
    for val in row:
        flat.append(val)
print(flat)  # [1,2,3,4,5,6,7,8,9]

# 6. Diagonal elements
diag = []
for i in range(len(matrix)):
    diag.append(matrix[i][i])
print(diag)  # [1, 5, 9]
