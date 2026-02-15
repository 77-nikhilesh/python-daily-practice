# 1. for-else without break
for i in range(1, 4):
    print(i)
else:
    print("Loop finished")
# Output:
# 1
# 2
# 3
# Loop finished

# 2. for-else with break
for i in range(1, 4):
    if i == 2:
        break
    print(i)
else:
    print("Completed")
# Output:
# 1
