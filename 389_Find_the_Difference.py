# python 389_Find_the_Difference.py

s = "a"
t = "aa"
s = "abcd"
t = "abcde"
# Output: "a"
big_item = s if len(s) > len(t) else t
small_item = s if len(s) < len(t) else t

count = {}


for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char in t:
    if char not in count or count[char] == 0:
        print(char)
    count[char] -= 1
