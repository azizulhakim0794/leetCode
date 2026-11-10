# python 462_Minimum_Moves_to_Equal_Array_Elements_II.py
# nums = [1, 2, 3]
nums = [1, 10, 2, 9, 0, 0]
# nums = [1, 3, 2]  # 2

# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# temp = 0
# count = 0

# for i in range(len(nums)):

#     temp = 0
#     num = nums[i]
#     for j in range(len(nums)):
#         # if num > nums[j] and i != j:
#         #     temp += num - nums[j]
#         # if num < nums[j] and i != j:
#         temp += abs(nums[j] - num)

#     if i == 0:
#         count = temp

#     if temp < count:
#         count = temp


# print(count)


nums.sort()

median = nums[len(nums) // 2]

count = 0

for num in nums:
    count += abs(num - median)

print(count)
