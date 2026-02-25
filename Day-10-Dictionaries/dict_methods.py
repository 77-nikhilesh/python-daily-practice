d = {"a": 10, "b": 20, "c": 30}

print(d.keys())                        # dict_keys(['a','b','c'])
print(d.values())                      # dict_values([10,20,30])
print(d.items())                       # dict_items(...)

# fromkeys()
keys = ["x", "y", "z"]
new = dict.fromkeys(keys, 0)
print(new)                             # {'x':0,'y':0,'z':0}

# setdefault()
d.setdefault("d", 40)
print(d)

# Copy
d2 = d.copy()
print(d2)