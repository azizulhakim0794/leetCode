# python 3712_Sum_of_Elements_With_Frequency_Divisible_by_K.py
nums = [1, 2, 2, 3, 3, 3, 3, 4]
k = 2

# Output: 16
# Explanation:
# The number 1 appears once (odd frequency).
# The number 2 appears twice (even frequency).
# The number 3 appears four times (even frequency).
# The number 4 appears once (odd frequency).
# So, the total sum is 2 + 2 + 3 + 3 + 3 + 3 = 16.

# count = {}
# buckets = [[] for _ in range(len(nums))]
# result = []
# sum = 0

# for num in nums:
#     count[num] = count.get(num, 0) + 1


# for num, freq in count.items():
#     if freq > 1:
#         buckets[freq].append(num)

# for i in range(len(buckets) - 1, 0, -1):
#     for num in buckets[i]:
#         result.append(num)

#         if len(result) == k:
#             break

#     if len(result) == k:
#         break

# for num in nums:
#     if num in result:
#         sum += num

# print(result, sum)


count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

total = 0

for num, freq in count.items():

    if freq % k == 0:
        total += num * freq

print(total)
