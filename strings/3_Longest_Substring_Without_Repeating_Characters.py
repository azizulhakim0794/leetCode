# python 3_Longest_Substring_Without_Repeating_Characters.py
s = "eeg"
# Output: 3

str_set = []
count = 0

for i in range(len(s)):
    while s[i] in str_set:
        str_set.pop(0)
        # left += 1

    str_set.append(s[i])

    if count < len(str_set):
        count = len(str_set)


print(len(str_set), count)


# str_set = set()
# count = 0
# left = 0

# for i in range(len(s)):

#     while s[i] in str_set:
#         str_set.remove(s[left])
#         left += 1

#     str_set.add(s[i])

#     if count < len(str_set):
#         count = len(str_set)

# print(count)
