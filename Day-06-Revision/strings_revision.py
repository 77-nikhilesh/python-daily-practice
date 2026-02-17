# 1. Reverse string
s = "python"
print(s[::-1])
# Output: nohtyp

# 2. Palindrome string
print("Palindrome" if s == s[::-1] else "Not Palindrome")
# Output: Not Palindrome

# 3. Count vowels
count = 0
for ch in "education":
    if ch in "aeiou":
        count += 1
print(count)
# Output: 5

# 4. Word count
sentence = "Python is easy to learn"
print(len(sentence.split()))
# Output: 5

# 5. Uppercase conversion
print(sentence.upper())
# Output: PYTHON IS EASY TO LEARN

# 6. Replace word
print(sentence.replace("easy", "powerful"))
# Output: Python is powerful to learn

# 7. Check numeric string
print("12345".isdigit())
# Output: True

# 8. Longest word
words = sentence.split()
print(max(words, key=len))
# Output: Python
