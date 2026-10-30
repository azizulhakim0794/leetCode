# python 205_Isomorphic_Strings.py
s = "egg"
t = "add"

# Output: true

# Create two empty hash maps.
# Loop through both strings at the same time using zip(s, t).
# If a character already exists in a map, check whether its mapping matches the current character.
# If either mapping conflicts, return False.
# If all characters match consistently, return True.

count = {}
count2 = {}

for i, j in zip(s, t):
    if i in count and count[i] != j:
        print(False)
    if j in count2 and count2[j] != i:
        print(False)

    count[i] = j
    count2[j] = i
    print(count[i], j, count2[j], i)


print(True)


# if len(s) != len(t):
#     print(False)

# count = {}
# count2 = {}

# for i in s:
#     count[i] = count.get(i, 0) + 1

# for j in t:
#     count2[j] = count2.get(j, 0) + 1

# if sorted(count.values()) == sorted(count2.values()):
#     print(True)
# else:
#     print(False)


# print(count.items())
