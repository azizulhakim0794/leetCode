# python 229_Majority_Element_II.py
nums = [1, 2, 3, 4]
# Output: 3

count = len(nums) // 3

map_Arr = {}
ans = []

for num in nums:
    if num in map_Arr:
        map_Arr[num] += 1
    if num not in map_Arr:
        map_Arr[num] = 1

for num in map_Arr:
    if map_Arr[num] > len(nums) // 3:
        ans.append(num)

print(ans)
