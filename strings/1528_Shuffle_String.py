# python 1528_Shuffle_String.py

s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
# leetcode


# ans = [""] * len(s)

# print(ans)

# for i in range(len(indices)):
#     ans[indices[i]] = s[i]
#     print(ans)

# # print("".join(ans))
# print(ans)


ans = ""

for i in range(len(indices)):
    for j in range(len(s)):
        if indices[j] == i:
            ans += s[j]
            break
print(ans)


# ans = [""] * len(s)

# for i in range(len(indices)):
#     for j in range(len(s)):
#         if i == indices[j]:
#             ans[i] = s[j]
#             break

# print("".join(ans))
