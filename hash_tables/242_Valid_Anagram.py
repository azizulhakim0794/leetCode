# python 242_Valid_Anagram.py

s = "anagram"
t = "nagaram"
# Output: true

# s = "rat"
# t = "car"
# Output: false

print(sorted(s) == sorted(t))
# print(sorted(t))
