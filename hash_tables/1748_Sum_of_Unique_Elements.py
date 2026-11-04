# python 1748_Sum_of_Unique_Elements.py
nums = [1, 2, 3, 4, 5]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

count = {}

sum = 0

for num in nums:
    count[num] = count.get(num, 0) + 1

print(count)

for num in nums:
    if count.get(num) == 1:
        sum += num

print(sum)
