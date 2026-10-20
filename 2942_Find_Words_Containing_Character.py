# python 2942_Find_Words_Containing_Character.py
words = ["leet", "code"]
x = "e"
# Output: [0,1]

ans = []

for i in range(len(words)):
    for j in words[i]:
        if j == x and i not in ans:
            ans.append(i)

print(ans)
