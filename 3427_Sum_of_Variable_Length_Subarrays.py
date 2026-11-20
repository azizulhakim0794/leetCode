# python3 3427_Sum_of_Variable_Length_Subarrays.py

nums = [3,1,1,2]

# Output: 13

ans = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        start = max(0, i - nums[i])
        if 0 <= i and i < nums[i]:
            ans +=  sum(nums[i:j+1])

            # print(nums[i+i:j+1])
# print(ans)