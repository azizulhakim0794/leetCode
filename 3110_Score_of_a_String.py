# python 3110_Score_of_a_String.py
s = "hello"

Output: 13

# print(ord("h"))

sum = 0

for i in range(len(s) - 1):
    first = ord(s[i])
    second = ord(s[i + 1])
    sum += abs(first - second)

print(sum)
