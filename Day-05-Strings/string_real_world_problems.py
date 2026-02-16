# 1. Palindrome check
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")
# Output: Palindrome

# 2. Count words in sentence
sentence = "Python is very powerful"
print(len(sentence.split()))
# Output: 4

# 3. Find longest word
words = sentence.split()
print(max(words, key=len))
# Output: powerful

# 4. Remove vowels
text = "education"
result = ""
for ch in text:
    if ch not in "aeiou":
        result += ch
print(result)
# Output: dctn

# 5. Replace spaces with hyphen
print(sentence.replace(" ", "-"))
# Output: Python-is-very-powerful

# 6. Email validation (basic)
email = "test@gmail.com"
print("Valid" if "@" in email and "." in email else "Invalid")
# Output: Valid

# 7. Count uppercase letters
text = "PyThOn"
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Uppercase:", count)
# Output: Uppercase: 3
