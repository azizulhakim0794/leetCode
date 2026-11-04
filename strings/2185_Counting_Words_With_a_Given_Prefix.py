# python 2185_Counting_Words_With_a_Given_Prefix.py
words = ["pay", "attention", "practice", "attend"]
pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

count = 0
for i in range(len(words)):
    if words[i][: len(pref)] == pref:
        count += 1

print(count)
