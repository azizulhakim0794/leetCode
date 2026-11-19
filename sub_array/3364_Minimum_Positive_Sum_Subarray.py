# python3 3364_Minimum_Positive_Sum_Subarray.py
nums = [3,-2,1,4]
l = 2
r = 3

# Output: 1

# Explanation:

# The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

# [3, -2] with a sum of 1
# [1, 4] with a sum of 5
# [3, -2, 1] with a sum of 2
# [-2, 1, 4] with a sum of 3
# Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

results = []
sum_arr = []
# print(sum(nums))

for i in range(len(nums)):
    for j in range(len(nums)):
        # print(nums[i:j+1])
        results.append(nums[i:j+1])

print(results)

if len(results) ==0:
    print(-1)


for i in range(len(results)):
    if len(results[i]) >=l and len(results[i]) <= r and sum(results[i]) > 0: 
        sum_arr.append(sum(results[i]))

# print(min(sum_arr))
if len(sum_arr)>0 and min(sum_arr) > 0:
    print(min(sum_arr))
else:
    print(-1)
# print(sum_arr)
    # for j in range(len(results[i])):
    #     print(results[i][j])