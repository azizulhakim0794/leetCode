# python 448_Find_All_Numbers_Disappeared_in_an_Array.py
# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1, 1, 3, 3]
# nums = [1, 2, 3, 4, 5]
# nums = [5, 5, 5, 5, 5]


# nums = [1, 1]

# Output: [5,6]

n = len(nums)

for num in nums:
    index = abs(num) - 1
    if nums[index] > 0:
        nums[index] = -nums[index]

ans = []

for i in range(n):
    if nums[i] > 0:
        ans.append(i + 1)

print(ans)
