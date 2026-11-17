# python 53_Maximum_Subarray.py

nums = [2, 1, 5, 1, 3]
subarrays = []

max_sum = float("-inf")

for i in range(len(nums)):
    for j in range(i, len(nums)):
        subarray = nums[i : j + 1]
        subarrays.append(subarray)
        current_sum = sum(subarray)

        max_sum = max(max_sum, current_sum)

print(subarrays, sum([3, 6]))
