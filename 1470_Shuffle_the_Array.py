# python 1470_Shuffle_the_Array.py
nums = [2, 5, 1, 3, 4, 7]
n = 3
# Output: [2,3,5,4,1,7]

# store = nums[1]
# nums[1] = nums[n]
# nums[n] = store

ans = []

for i in range(int(len(nums) / 2)):
    next_i = i + n
    ans.append(nums[i])
    ans.append(nums[next_i])

print(ans)
