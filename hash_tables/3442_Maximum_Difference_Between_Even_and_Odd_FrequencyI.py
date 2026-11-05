# python 3442_Maximum_Difference_Between_Even_and_Odd_FrequencyI.py
s = "mmsmsym"

# Output: 3
# Explanation:
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.


count = {}
max_odd = 0
min_even = float("inf")

for char in s:
    count[char] = count.get(char, 0) + 1


print(count)
for char, freq in count.items():
    if freq % 2 == 1:
        max_odd = max(max_odd, freq)

    else:
        min_even = min(min_even, freq)

print(max_odd, min_even)
