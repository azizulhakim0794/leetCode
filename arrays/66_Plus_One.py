# python 66_Plus_One.py

digits = [1, 2, 3]
# Output: [1,2,4]

num = ""
ans = []

for i in range(len(digits)):
    num += str(digits[i])

add_last = str((int(num)) + 1)

for i in range(len(add_last)):
    ans.append(int(add_last[i]))

print(ans)
