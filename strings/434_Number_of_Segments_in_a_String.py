# python 434_Number_of_Segments_in_a_String.py
# s = "Hello, my name is John"
# Output: 5
# s = "a"
s = "a, b, c"
# s = "                "

# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

results = []
word = ""
length = 0

for i in range(len(s)):
    if len(s) == 1 and s[0] != " ":
        print(1)
    if s[i] == " " or (i == len(s) - 1 and s[i] != " "):
        if i == len(s) - 1 and s[i] != " ":
            word = s[i]
        results.append(word)
        word = ""
        continue
    word += s[i]

for i in range(len(results)):
    if results[i] != "":
        length += 1

print(results, length, len(s))
