# python 169_Majority_Element.py
nums = [3, 2, 3]
# Output: 3

# nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2


# for num in nums:
#     if nums.count(num) > len(nums) // 2:
#         print(num)
#         break

nums = [2, 2, 1, 1, 1, 2, 2]

# repted_Item = None
# count = 0

# for num in nums:
#     if count == 0:
#         repted_Item = num

#     if num == repted_Item:
#         count += 1
#     else:
#         count -= 1

# return repted_Item

nums.sort()
print(nums[len(nums) // 2])
