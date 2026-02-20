a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union
print(a | b)                   # {1, 2, 3, 4, 5, 6}

# Intersection
print(a & b)                   # {3, 4}

# Difference
print(a - b)                   # {1, 2}

# Symmetric Difference
print(a ^ b)                   # {1, 2, 5, 6}

# Subset & Superset
print({1, 2}.issubset(a))      # True
print(a.issuperset({1, 2}))    # True

# Disjoint
print(a.isdisjoint({7, 8}))    # True