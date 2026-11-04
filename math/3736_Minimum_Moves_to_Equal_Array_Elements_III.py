# python 3736_Minimum_Moves_to_Equal_Array_Elements_III.py

nums = [4, 4, 5]

# Output: 3

# Explanation:
# To make all elements equal:
# Increase nums[0] = 2 by 1 to make it 3.
# Increase nums[1] = 1 by 1 to make it 2.
# Increase nums[1] = 2 by 1 to make it 3.
# Now, all elements of nums are equal to 3. The minimum total moves is 3.

total = 0

for num in nums:
    total += abs(num - max(nums))


print(total)
