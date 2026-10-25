# python Difference_Between_Peaks_and_Valleys.py
nums = [6, 5, 2, 5, 5, 3, 6]

# Output: 9

# You are given an integer array nums of length n.

# An index i is called a peak if all of the following conditions hold
# 0 < i < n - 1
# nums[i] > nums[i - 1]
# nums[i] > nums[i + 1]
# An index i is called a valley if all of the following conditions hold:

# 0 < i < n - 1
# nums[i] < nums[i - 1]
# nums[i] < nums[i + 1]
# Return an integer denoting the difference between the sum of all peak values
# and the sum of all valley values.
peak = 0
valley = 0

for i in range(len(nums) - 1):
    if (
        (nums[i] > nums[i - 1] and nums[i] > nums[i + 1])
        and 0 < i
        and i < len(nums) - 1
    ):
        peak += nums[i]
    if (
        (nums[i] < nums[i - 1] and nums[i] < nums[i + 1])
        and 0 < i
        and i < len(nums) - 1
    ):
        valley += nums[i]


print(peak - valley)
