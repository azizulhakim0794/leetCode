# python 290_Word_Pattern.py
# pattern = "abba"
# s = "dog cat cat dog"

pattern = "aaaa"
s = "dog cat cat dog"
# Output: true

# pattern = "abba"
# s = "dog cat cat fish"
# Output: false

count = {}
count2 = {}

str_arr = s.split()

if len(pattern) != len(str_arr):
    print(False)

for i, char in enumerate(pattern):
    if char not in count:
        count[char] = []

    count[char].append(i)

for i, word in enumerate(str_arr):
    if word not in count2:
        count2[word] = []
    count2[word].append(i)

if len(count) != len(count2):
    print(False)

if sorted(count.values()) == sorted(count2.values()):
    print(True)

print(False)
