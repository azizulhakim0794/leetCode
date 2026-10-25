# python 1859_Sorting_the_Sentence.py
s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"

degites = "123456789"
new_s = ""
order = []
new_Arr = []

for i in range(len(s)):
    if s[i] in degites:
        order.append(int(s[i]) - 1)
    else:
        new_s += s[i]

strArr = new_s.split()

for j in range(len(strArr)):
    for k in range(len(order)):
        if j == order[k]:
            new_Arr.append(strArr[k])


print(" ".join(new_Arr))


s = "is2 sentence4 This1 a3"

degites = "123456789"
new_s = ""
order = []
new_Arr = []

for i in range(len(s)):
    if s[i] in degites:
        order.append(int(s[i]) - 1)
    else:
        new_s += s[i]

strArr = new_s.split()

new_Arr = [""] * len(strArr)

for k in range(len(order)):
    new_Arr[order[k]] = strArr[k]

print(" ".join(new_Arr))
