# python Q2_Count_Subarrays_With_Loose_Bounds.py

nums = [1, 4, 2, 7, 3]
minK = 1
maxK = 5

# Output: [1], [4], [1,4], [2], [1,4,2] [4,2], [3]

# 1 4 3
count = 0
ans = 0
for i in range(len(nums)):
    if nums[i] >= minK and nums[i] <= maxK:
        count += 1
        ans += count
    else:
        count = 0

print(ans)
