# python 1002_Find_Common_Characters.py

words = ["bella", "label", "roller"]
# # Output: ["e","l","l"]


ans = []

f_words = words[0]

for i in range(1, len(words)):
    for j in range(len(words[i])):
        item = words[i].find(words[(i - 1)][j])
        if item:
            ans.append(words[i][j])
    # for j in words[i]:


# for i in range(len(words) - 1):
#     for j in range(i + 1, len(words)):
#         if words[i] == words[j]:
#             ans.append(words[j])

print(ans)
