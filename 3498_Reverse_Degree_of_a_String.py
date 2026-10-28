# python 3498_Reverse_Degree_of_a_String.py

s = "abc"
# Output: 148

letter = "abcdefghijklmnopqrstuvwxyz"
alpha = {}

sum = 0

for i in range(len(letter)):
    alpha[letter[i]] = alpha.get(letter[i], 0) + len(letter) - i


for j in range(len(s)):

    sum += alpha[s[j]] * (j + 1)

print(sum)
