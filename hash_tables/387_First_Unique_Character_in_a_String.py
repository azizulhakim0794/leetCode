# python 387_First_Unique_Character_in_a_String.py

s = "dddccdbba"
# Output: 0

count = {}

for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for i in range(len(s)):
    item = count[s[i]]

    if item == 1:
        print(i)
        break
else:
    print(-1)
