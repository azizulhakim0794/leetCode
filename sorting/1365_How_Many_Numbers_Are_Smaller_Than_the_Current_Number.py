# python 1365_How_Many_Numbers_Are_Smaller_Than_the_Current_Number.py
nums = [8, 1, 2, 2, 3]
# Output: [4,0,1,1,3]
nums = [7, 7, 7, 7]

ans = []

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):

        if (
            nums[i] > nums[j] or (nums[i] == nums[j]) and nums[i] not in nums
        ) and i != j:
            count += 1
    ans.append(count)

print(ans)
