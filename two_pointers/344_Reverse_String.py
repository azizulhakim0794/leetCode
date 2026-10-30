# python 344_Reverse_String.py
# import json

s = ["h", "e", "l", "l", "o"]

ans = []
for i in range(len(s)):
    ans.append(s[len(s) - (1 + i)])

s.reverse()
print(s)
