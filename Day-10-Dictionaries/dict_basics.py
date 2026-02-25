# Dictionary creation
student = {"id": 101, "name": "Nikhilesh", "age": 21}
print(student)                         # {'id': 101, 'name': 'Nikhilesh', 'age': 21}

# Empty dictionary
empty = {}
print(type(empty))                     # <class 'dict'>

# Using dict()
data = dict(a=10, b=20)
print(data)                            # {'a': 10, 'b': 20}

# Length
print(len(student))                    # 3

# Duplicate keys overwrite
dup = {"a": 1, "a": 2}
print(dup)                             # {'a': 2}