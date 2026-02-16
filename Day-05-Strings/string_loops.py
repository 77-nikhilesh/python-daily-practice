# 1. Print each character
for ch in "Python":
    print(ch, end=" ")
# Output: P y t h o n

print()

# 2. Count vowels
text = "education"
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)
# Output: Vowels: 5

# 3. Reverse string using loop
rev = ""
for ch in "Python":
    rev = ch + rev
print(rev)
# Output: nohtyP

# 4. Count consonants
count = 0
for ch in "python":
    if ch not in "aeiou":
        count += 1
print("Consonants:", count)
# Output: Consonants: 4

# 5. Index-based loop
s = "Loop"
for i in range(len(s)):
    print(s[i], end=" ")
# Output: L o o p

print()

# 6. Character frequency
text = "hello"
for ch in set(text):
    print(ch, ":", text.count(ch))
