# 26_Remove_Duplicates_from_Sorted_Array.py
nums = [1, 1, 2]
# Output: 2, nums = [1,2,_]

ans = []
for i in range(len(nums)):
    if nums[i] not in ans:
        ans.append(nums[i])

ans = sorted(ans)

for i in range(len(ans)):
    nums[i] = ans[i]

print(len(ans))
