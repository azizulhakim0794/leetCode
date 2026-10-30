# python 3925_Concatenate_Array_With_Reverse.py

nums = [1, 2, 3]

# Output: [1,2,3,3,2,1]

ans = nums.copy()

n = len(nums)

for i in range(n):
    ans.append(nums[n - i - 1])

print(ans)
