# python 283_Move_Zeroes.py
nums = [0, 1, 0, 3, 12]
# Output: [1,3,12,0,0]

# nums = [-1, 0, -3, 0, 5]
# Output: [-1,-3,5,0,0]

# nums.append(20)
# print(nums)

zeros = []


for i in range(len(nums)):
    if nums[i] == 0:
        zeros.append(nums[i])

nums[:] = [n for n in nums if n != 0]

for j in range(len(zeros)):
    nums.append(zeros[j])

print(nums)
