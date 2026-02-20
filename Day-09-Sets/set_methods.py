s = {10, 20, 30}

# add()
s.add(40)
print(s)                       # {10, 20, 30, 40}

# update()
s.update([50, 60])
print(s)                       # {10, 20, 30, 40, 50, 60}

# remove()
s.remove(20)
print(s)                       # {10, 30, 40, 50, 60}

# discard()
s.discard(100)                 # No error

# pop()
removed = s.pop()
print(removed)                 # Random element

# clear()
temp = {1, 2, 3}
temp.clear()
print(temp)                    # set()