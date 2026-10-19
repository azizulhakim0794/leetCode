# python 645_Set_Mismatch.py
# check the before and current item in a loop


# nums = [1, 2, 2, 4]
# Output: [2,3]
# nums = [1, 2, 2, 2, 3]

# nums = [3, 3, 4, 4]
# Output : [2,1]

# nums = [2, 2]
# Output: [2,1]

# nums = [3, 2, 2]
# nums = [1, 3, 3]
# Output: [3,2]

nums = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]
# [3,1]

duplicate = 0
missing = 0

nums.sort()

for i in range(len(nums)):
    if nums[i - 1] == nums[i]:
        duplicate = nums[i]


for i in range(len(nums)):
    if (i + 1) not in nums:
        missing = i + 1
        break

print([duplicate, missing])
print(nums)
