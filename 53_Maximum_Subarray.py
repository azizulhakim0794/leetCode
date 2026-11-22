# python3 53_Maximum_Subarray.py
# nums = [-2,-1]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1,2,3]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


sub_arry = []

total = nums[0]

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if len(nums[i:j+1]) > 0:
#             sum_arr = sum(nums[i:j+1])
#             sub_arry.append(nums[i:j+1])
#             if total < sum_arr:
#                 total = sum_arr

def get_subarrays(nums, start=0, end=1):
    if start == len(nums):
        return []

    if end > len(nums):
        return get_subarrays(nums, start + 1, start + 2)
    print([nums[start:end]])
    return [nums[start:end]] + get_subarrays(nums, start, end + 1)

sub_arry = (get_subarrays(nums))

for i in range(len(sub_arry)):
    total_sum = sum(sub_arry[i])
    if total < sum(sub_arry[i]):
        total = total_sum

print(total)

print([1] + [1, 2])
