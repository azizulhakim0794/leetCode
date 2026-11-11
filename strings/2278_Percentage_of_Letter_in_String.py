# python 2278_Percentage_of_Letter_in_String.py
import math

s = "kkkk"
letter = "o"
# Output: 33

count = 0

for char in s:
    if char == letter:
        count += 1

persentage = math.floor(count / len(s) * 100)

print(persentage)
