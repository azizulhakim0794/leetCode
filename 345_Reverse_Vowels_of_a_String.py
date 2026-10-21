# python 345_Reverse_Vowels_of_a_String.py

s = "IceCreAm"
# Output: "AceCreIm"

vol = []

ans = ""

for i in s:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        vol.append(i)

for j in range(len(s)):
    if s[j].lower() in ["a", "e", "i", "o", "u"]:
        ans += vol[-1]
        vol.pop()
    else:
        ans += s[j]

print(ans)
