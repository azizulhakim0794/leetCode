# python 2089_Find_Target_Indices_After_Sorting_Array.py
nums = [1, 2, 2, 3, 5]
target = 3
# Output: [1,2]

nums.sort()

ans = []

for i in range(len(nums)):
    if nums[i] == target:
        ans.append(i)

print(ans)
