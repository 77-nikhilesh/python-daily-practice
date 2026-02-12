"""
Problem: Track daily task completion percentage using assignment operators.

"""

progress = 10
print("Initial Progress:", progress)

progress += 20
progress -= 5
progress *= 2
progress /= 5
progress //= 2
progress %= 7
progress **= 2

print("Final Progress:", int(progress))

# Output:
# Initial Progress: 10
# Final Progress: 4
