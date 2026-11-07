# python 500_Keyboard_Row.py

words = ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska","Dad"]

rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

result = []


text = set(words[1].lower()).issubset(rows[1])
print(text)

for word in words:
    word_set = set(word.lower())
    for row in rows:
        if word_set.issubset(row):
            result.append(word)
print(result)


# for word in words:
#     word_set = set(word.lower())

#     for row in rows:
#         if word_set.issubset(row):
#             result.append(word)
#             break

# print(result)
