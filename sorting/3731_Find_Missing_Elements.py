# python 3731_Find_Missing_Elements.py
nums = [1, 4, 2, 5]

# Output: [3]

max_num = max(nums)
min_num = min(nums)

# print(max_num, min_num)
ans = []
nums1 = set(nums)
for i in range(min_num, max_num + 1):
    if i not in nums1:
        ans.append(i)

print(ans)
