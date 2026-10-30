# python 27_Remove_Element.py
nums = [3, 2, 2, 3]
val = 3
# Output: 2, nums = [2,2,_,_]

ans = []

for i in range(len(nums)):
    if nums[i] != val:
        ans.append(nums[i])

ans = sorted(ans)

print(ans)
