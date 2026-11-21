# python3 3427_Sum_of_Variable_Length_Subarrays.py

nums = [3,1,1,2]
# nums = [5, 5, 5, 5] # 50

# Output: 13

ans = 0

for i in range(len(nums)):
    start = max(0, i - nums[i])
    if 0 <= i and i < len(nums):
        ans+= sum(nums[start : i+1])
        print(nums[start : i+1])

print(ans)