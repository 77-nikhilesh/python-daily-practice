"""
Problem: Manage system permissions using bitwise operators.

"""

read = 4     # 100
write = 2    # 010
execute = 1  # 001

print("AND (&):", read & write)
print("OR (|):", read | write)
print("XOR (^):", read ^ write)
print("NOT (~read):", ~read)
print("Left Shift (read << 1):", read << 1)
print("Right Shift (read >> 1):", read >> 1)

# Output:
# AND (&): 0
# OR (|): 6
# XOR (^): 6
# NOT (~read): -5
# Left Shift (read << 1): 8
# Right Shift (read >> 1): 2
