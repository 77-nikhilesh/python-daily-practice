t1 = (1, 2, 3)
t2 = (4, 5)

print(t1 + t2)           # (1, 2, 3, 4, 5)
print(t1 * 3)            # (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(2 in t1)           # True
print(10 in t1)          # False

# Iteration
for item in t1:
    print(item, end=" ") # 1 2 3
