"""
Problem: Verify whether variables point to the same memory location.

"""

a = [10, 20, 30]
b = [10, 20, 30]
c = a

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not b:", a is not b)

# Output:
# a is b: False
# a is c: True
# a is not b: True
