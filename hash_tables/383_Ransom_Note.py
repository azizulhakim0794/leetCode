# python 383_Ransom_Note.py

ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
# Output: true

count = {}
count2 = {}

ans = ""

for i in range(len(magazine)):
    count[magazine[i]] = count.get(magazine[i], 0) + 1

for i in range(len(ransomNote)):
    count2[ransomNote[i]] = count2.get(ransomNote[i], 0) + 1

for i in count2:
    if count.get(i, 0) > count2[i]:
        print(False)


print(True)


#     print(count[i], i)

# print(count, count2)
