# python 344_Reverse_String.py
# import json

s = ["h", "e", "l", "l", "o"]

# ans = []
# for i in range(len(s)):
#     ans.append(s[len(s) - (1 + i)])

# # s.reverse()
# print(ans)


def recursive_string(s):
    if len(s) == 0:
        return s

    return recursive_string(s[1:]) + [s[0]]


print(recursive_string(s))
